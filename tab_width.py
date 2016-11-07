#!/usr/bin/python
# !/usr/bin/python2.7
# !/usr/bin/python3

import argparse

from checks import tab_width

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Identify lines not indented by a multiple of N spaces."
    )

    parser.add_argument(
        '--width', metavar=4, default=4, type=int,
        help='The number of spaces required in a tabulation.'
    )

    parser.add_argument(
        'path', metavar='/path/to/package',
        help='Path to the package folder.'
    )

    # Parse command line
    args = parser.parse_args()

    # Rename arguments for convenience
    pkgDir = args.path
    width = args.width

    tab_width.main(pkgDir, width)
