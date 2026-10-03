"""Steam Screenshot Sort — Sort Steam screenshots into folders by app id or date."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='steam_screenshot_sort',
        description='Sort Steam screenshots into folders by app id or date.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Steam Screenshot Sort')
    print('Screenshots out of the remote dump pile.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
