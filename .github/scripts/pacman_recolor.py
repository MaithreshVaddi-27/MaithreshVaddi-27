#!/usr/bin/env python3
"""Recolor pacman-contribution-graph SVGs to the maithresh.pages.dev Cobalt ramp.

The abozanona action exposes no theme input, so it always emits stock
GitHub greens inside SMIL <animate values="..."> attributes. This script
rewrites contribution-level and empty-cell tokens, preserving luminance order:

  dark  empty #161b22 -> #171C26
        #0e4429 -> #172554,  #006d32 -> #1E40AF,
        #26a641 -> #2563EB,  #39d353 -> #60A5FA   (maithresh.pages.dev dark ramp)
  light empty #ebedf0 -> #EAE4DA
        #9be9a8 -> #93C5FD,  #40c463 -> #60A5FA,
        #30a14e -> #2563EB,  #216e39 -> #1E40AF   (Monograph light paper ramp)

Untouched by design: pellets, month labels, and Pac-Man/ghost character
animations (yellow/red/#808).

Run from repo root after the generate step (expects dist/*.svg).
Zero dependencies. Fails loud (exit 1) when dist/ is empty.
"""
import glob
import re
import sys

MAP = {
    '#161b22': '#171C26',
    '#0e4429': '#172554',
    '#006d32': '#1E40AF',
    '#26a641': '#2563EB',
    '#39d353': '#60A5FA',
    '#ebedf0': '#EAE4DA',
    '#9be9a8': '#93C5FD',
    '#40c463': '#60A5FA',
    '#30a14e': '#2563EB',
    '#216e39': '#1E40AF',
}

PAT = re.compile('|'.join(sorted(MAP)), re.IGNORECASE)


def process(path):
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    txt, n = PAT.subn(lambda m: MAP[m.group(0).lower()], txt)
    if not n:
        print(f'skip {path}: no contribution tokens found')
        return False
    with open(path, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f'ok {path}: recolored {n} tokens')
    return True


def main():
    files = sorted(glob.glob('dist/*.svg'))
    if not files:
        print('no dist/*.svg found')
        return 1
    ok = all(process(p) for p in files)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
