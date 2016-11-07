#!/usr/bin/python
# !/usr/bin/python2.7
# !/usr/bin/python3

import argparse

from utils import files


def checkLines(list, max_length):
    """Returns indices of lines where length is above allowance."""
    problems = []
    for i in range(len(list)):
        lineLength = len(list[i])
        if lineLength > max_length:
            problems.append((i, lineLength))
    return problems


def checkFile(pkgRootDir, file, max_length):
    '''Checks all the lines of a file for length.'''
    trimmedFile = file[(len(pkgRootDir)+1):]
    with open(file, 'r') as f:
        lines = f.readlines()
        problems = checkLines(lines, max_length)
    for pb in problems:
        print("%s\t(line %i)\t%i chars" % (trimmedFile, pb[0], pb[1]))
    return len(problems)


def check(pkgRootDir, files, max_length):
    '''Check all the files for length.'''
    total = 0

    print "  * Searching for lines > %i characters *\n" % max_length

    for file in files:
        total += checkFile(pkgRootDir, file, max_length)

    print("\n=== Summary: %i lines > %i characters long. ===\n" % (total, max_length))
    return total


def main(path, max_char):
    # List files to check
    checkFiles = files.listPackageFiles(path)
    # call script to check line length
    check(path, checkFiles, max_char)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Identify lines > N characters long."
    )

    parser.add_argument(
        '--max_char', metavar='N', default=80, type=int,
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
    max_char = args.max_char

    main(pkgDir, max_char)
