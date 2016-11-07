#!/usr/bin/python
# !/usr/bin/python2.7
# !/usr/bin/python3

# usage:
# script.py rootFolder filesFile


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
        print("%s\t(line %i): %i chars" % (trimmedFile, pb[0], pb[1]))
    return len(problems)


def check(pkgRootDir, files, max_length):
    '''Check all the files for length.'''
    total = 0

    print "  * Searching for lines > %i characters *\n" % max_length

    for file in files:
        total += checkFile(pkgRootDir, file, max_length)

    print("\n=== Summary: %i lines > %i characters long. ===" % (total, max_length))
