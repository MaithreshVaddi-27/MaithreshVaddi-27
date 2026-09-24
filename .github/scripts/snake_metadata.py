#!/usr/bin/env python3
"""Inject maithresh.sh terminal metadata bars into snk-generated SVGs.

Top bar:    maithresh.sh: snake --contributions      @MaithreshVaddi-27
Bottom bar: SEP 2025 — SEP 2026                      REGEN SEP 24, 2026 · DAILY

Run from repo root after the snk step (expects dist/*.svg).
Zero dependencies. Dark files get slate-400 text, light files slate-600.
"""
import glob
import re
import sys
from datetime import datetime, timezone

TOP, BOT = 34, 30
FONT = 'JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace'
MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


def process(path, start, end, datestr):
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', txt)
    if not m:
        print(f'skip {path}: no viewBox')
        return False
    minx, miny, w, h = (float(v) for v in m.groups())
    nh = h + TOP + BOT
    dark = 'dark' in path.split('/')[-1]
    tcol = '#94A3B8' if dark else '#475569'
    faint = '#64748B' if dark else '#94A3B8'

    head_end = txt.find('>', txt.find('<svg')) + 1
    head, inner = txt[:head_end], txt[head_end:txt.rfind('</svg>')]
    head = re.sub(r'viewBox="[-\d.]+ [-\d.]+ [\d.]+ [\d.]+"',
                  f'viewBox="{minx:g} {miny:g} {w:g} {nh:g}"', head, count=1)
    head = re.sub(r'\bheight="[\d.]+"', f'height="{nh:g}"', head, count=1)

    wi = lambda v: f'{v:g}'
    bar = (
        f'<g font-family="{FONT}">'
        f'<text x="{wi(minx + 4)}" y="{wi(miny + 20)}" font-size="12" font-weight="700" fill="#38BDF8">maithresh.sh: snake --contributions</text>'
        f'<text x="{wi(minx + w - 4)}" y="{wi(miny + 20)}" font-size="11" fill="{tcol}" text-anchor="end">@MaithreshVaddi-27</text>'
        f'<text x="{wi(minx + 4)}" y="{wi(miny + nh - 8)}" font-size="11" fill="{tcol}">{start} — {end}</text>'
        f'<text x="{wi(minx + w - 4)}" y="{wi(miny + nh - 8)}" font-size="11" fill="{faint}" text-anchor="end">REGEN {datestr} · DAILY</text>'
        f'</g>'
    )
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f'{head}<g transform="translate(0,{TOP})">{inner}</g>{bar}</svg>\n')
    print(f'ok {path}: {w:g}x{h:g} -> {w:g}x{nh:g}')
    return True


def main():
    now = datetime.now(timezone.utc)
    end = f'{MONTHS[now.month - 1]} {now.year}'
    start = f'{MONTHS[now.month - 1]} {now.year - 1}'
    datestr = now.strftime('%b %d, %Y').upper()
    files = sorted(glob.glob('dist/*.svg'))
    if not files:
        print('no dist/*.svg found')
        return 1
    ok = all(process(p, start, end, datestr) for p in files)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
