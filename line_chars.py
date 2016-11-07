#!/usr/bin/python
#!/usr/bin/python2.7
#!/usr/bin/python3

# usage:
# script.py rootFolder filesFile

import argparse
import os
import os.path
import re

parser = argparse.ArgumentParser(description='Check files for indentation by \
multiples of 4 spaces.')

parser.add_argument('--root', metavar='rootFolder', default=".",
    help='The folder to which all file paths are relative to.')

parser.add_argument('--max', metavar='N', default=80, type=int,
    help='The maximum number of characters allowed per line.')

parser.add_argument('filesFile', metavar='listFiles.txt',
    help='The file listing files to check.')             

#parser.print_help()

args = parser.parse_args()
#print(args)

#print(os.listdir(args.root))

files_to_check = open(args.filesFile, 'r').read().splitlines() 

#print(files_to_check)

total = 0 # counter for number of mis-indented lines

def checkLines(list, max_length):
    '''Returns indices of lines where indent is different than multiple of
    4-space'''
    problems = []
    for i in range(len(list)):
        if (len(list[i]) > max_length):
            problems.append(i)
    return(problems)

def checkFile(path, file, max_length):
    '''Checks all the lines of a file for 4 space indentation.'''
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        indices_problem = checkLines(lines, max_length)
    for i in indices_problem:
        print("%s\t(line %i)" % (file, i+1)) # lines[i].strip()
    return(len(indices_problem))

for file in files_to_check:
    #print(file)
    #print(os.path.join(args.root, file))
    #print(os.path.isfile(os.path.join(args.root, file)))
    total += checkFile(args.root, file, args.max)

print("%i lines over %i characters long" % (total, args.max))
