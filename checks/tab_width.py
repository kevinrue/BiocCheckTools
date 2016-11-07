#!/usr/bin/python
#!/usr/bin/python2.7
#!/usr/bin/python3

import argparse
import re

from utils import files


def checkLines(list, tab_width):
    """Returns indices of lines where indent is different than multiple of N space"""
    problems = []
    for i in range(len(list)):
        numSpaces = re.search(r'[^ ]', list[i]).start()
        if numSpaces % tab_width != 0:
            problems.append((i, numSpaces))
    return problems


def checkFile(path, file, tab_width):
    """Checks all the lines of a file for indents multiple of N spaces."""
    with open(file, 'r') as f:
        lines = f.readlines()
        problems = checkLines(lines, tab_width)
    for pb in problems:
        print("%s\t(line %i)\t%i spaces" % (file, pb[0], pb[1]))
    return len(problems)


def check(pkgRootDir, files, tab_width):
    """Check all the files for tab width."""
    total = 0

    print "  * Searching for lines not indented by a multiple of %i spaces *\n" % tab_width

    for file in files:
        total += checkFile(pkgRootDir, file, tab_width)

    print("\n=== Summary: %i lines not indented by a multiple of %i spaces. ===\n" % (total, tab_width))
    return total


def main(path, tab_width):
    # List files to check
    checkFiles = files.listPackageFiles(path)
    # call script to check line length
    check(path, checkFiles, tab_width)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Identify lines not indented y a multiple of N spaces."
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
    tab_width = args.tab_width

    main(pkgDir, tab_width)
