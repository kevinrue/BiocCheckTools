#!/usr/bin/python
#!/usr/bin/python2.7
#!/usr/bin/python3

import argparse

from checks import line_chars
from checks import tab_width
from checks.utils import files


def main(path, chars, tab):
    # List files to check
    checkFiles = files.listPackageFiles(pkgDir)
    # call script to check line length
    lineCharsCount = line_chars.check(pkgDir, checkFiles, chars)
    # call script to check tabulation width
    tabWidthCount = tab_width.check(pkgDir, checkFiles, tab)
    print "\n=== Global summary ==="
    print "  %i lines > %i characters long." % (lineCharsCount, chars)
    print "  %i lines not indented by multiple of %i spaces." % (tabWidthCount, tab)
    print ""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Identify lines offending certain Bioconductor guidelines."
    )

    parser.add_argument(
        '--max_char', metavar=80, default=80, type=int,
        help='The maximum number of characters allowed in a line.'
    )

    parser.add_argument(
        '--tab_width', metavar=4, default=4, type=int,
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
    chars = args.max_char
    tab = args.tab_width

    main(pkgDir, chars, tab)
