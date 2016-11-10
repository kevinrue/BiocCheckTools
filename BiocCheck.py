#!/usr/bin/python
#!/usr/bin/python2.7
#!/usr/bin/python3

import argparse

from checks import line_chars
from checks import tab_width
from checks.utils import files

validModes = ("all", "line_chars", "tab_width")


def main(path, mode, chars, tab):
    # Check inputs
    if not mode in validModes:
        raise ValueError("Invalid --mode value: %s" % mode)

    # List files to check
    checkFiles = files.listPackageFiles(pkgDir)

    # Collect and display individual reports
    reports = {}
    # call script to check line length, if requested
    if mode in ("all", "line_chars"):
        reports["lineChars"] = line_chars.check(pkgDir, checkFiles, chars)
    # call script to check tabulation width, if requested
    if mode in ("all", "tab_width"):
        reports["tabWidth"] = tab_width.check(pkgDir, checkFiles, tab)

    # Display global report
    if mode == "all":
        print "\n=== Global summary ==="
        if "lineChars" in reports.keys():
            print "  %i lines > %i characters long." % (reports["lineChars"], chars)
        if "tabWidth" in reports.keys():
            print "  %i lines not indented by multiple of %i spaces." % (reports["tabWidth"], tab)
        print ""

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Identify lines offending certain Bioconductor guidelines."
    )

    parser.add_argument(
        '--mode', metavar="all", default="all", type=str,
        help='Modules to run. Choices: all, line_chars, tab_width.'
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
    mode = args.mode
    chars = args.max_char
    tab = args.tab_width

    main(pkgDir, mode, chars, tab)
