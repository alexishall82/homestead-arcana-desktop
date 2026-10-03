"""Homestead Arcana Desktop — A local helper for Homestead Arcana cottage folders, spell notes, and garden photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='homestead_arcana_desktop',
        description='A local helper for Homestead Arcana cottage folders, spell notes, and garden photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Homestead Arcana Desktop')
    print('Keep the cottage on disk before a spell patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
