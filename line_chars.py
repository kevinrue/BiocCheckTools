#!/usr/bin/python
# !/usr/bin/python2.7
# !/usr/bin/python3

import argparse

from checks import line_chars

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Identify lines > N characters long."
    )

    parser.add_argument(
        '--chars', metavar=80, default=80, type=int,
        help='The maximum number of characters allowed in a line.'
    )

    parser.add_argument(
        'path', metavar='/path/to/package',
        help='Path to the package folder.'
    )

    # Parse command line
    args = parser.parse_args()

    # Rename arguments for convenience
    pkgDir = args.path
    chars = args.chars

    line_chars.main(pkgDir, chars)
