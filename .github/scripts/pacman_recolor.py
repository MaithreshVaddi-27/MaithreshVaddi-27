#!/usr/bin/env python3
"""Recolor pacman-contribution-graph SVGs to the maithresh.sh cyan ramp.

The abozanona action exposes no theme input, so it always emits stock
GitHub greens inside SMIL <animate values="..."> attributes. This script
rewrites ONLY those contribution-level tokens, preserving luminance order:

  dark  #0e4429 -> #134E6F,  #006d32 -> #1B7FB8,
        #26a641 -> #38BDF8,  #39d353 -> #BAE6FD   (maithresh.sh dot ramp)
  light #9be9a8 -> #BAE6FD,  #40c463 -> #38BDF8,
        #30a14e -> #0284C7,  #216e39 -> #0C4A6E

Untouched by design: empty-cell bases (#161B22 / #EBEDF0), pellets,
month labels, Pac-Man/ghost character animations (yellow/red/#808).

Run from repo root after the generate step (expects dist/*.svg).
Zero dependencies. Fails loud (exit 1) when dist/ is empty.
"""
import glob
import re
import sys

MAP = {
    '#0e4429': '#134E6F',
    '#006d32': '#1B7FB8',
    '#26a641': '#38BDF8',
    '#39d353': '#BAE6FD',
    '#9be9a8': '#BAE6FD',
    '#40c463': '#38BDF8',
    '#30a14e': '#0284C7',
    '#216e39': '#0C4A6E',
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
