#!/usr/bin/python
#!/usr/bin/python2.7
#!/usr/bin/python3

# usage:
# script.py rootFolder filesFile

import argparse
import glob
import os

parser = argparse.ArgumentParser(
    description="Identify lines offending certain Bioconductor guidelines."
)

parser.add_argument(
    '--max_char', metavar='length', default=80, type=int,
    help='The maximum number of characters allowed per line.'
)

parser.add_argument(
    '--tab_width', metavar='width', default=4, type=int,
    help='The number of spaces required in a tabulation.'
)

parser.add_argument('path', metavar='/path/to/package',
    help='Path to the package folder.')

args = parser.parse_args()

print("Package path:\t\t%s" % args.path)
print("Max characters:\t\t%i" % args.max_char)
print("Tabulation width:\t%s" % args.tab_width)

pkgDir = args.path

checkFiles = []

# Add DESCRIPTION file to check list ----

DESCRIPTIONfile = os.path.join(pkgDir, "DESCRIPTION")

if not os.path.exists(DESCRIPTIONfile):
    raise IOError("DESCRIPTION file not found in %s" % pkgDir)

checkFiles.append(DESCRIPTIONfile)

# Add NAMESPACE file to check list ----

NAMESPACEfile = os.path.join(pkgDir, "NAMESPACE")

if not os.path.exists(DESCRIPTIONfile):
    raise IOError("NAMESPACE file not found in %s" % pkgDir)

checkFiles.append(DESCRIPTIONfile)

# Find *.R files in R/ subdirectory ----

Rfolder = os.path.join(pkgDir, "R")

if not os.path.exists(Rfolder):
    raise IOError("R/ subdirectory not found in %s" % Rfolder)

if not os.path.isdir(Rfolder):
    raise IOError("%s is not a directory" % Rfolder)

Rfiles = glob.glob(os.path.join(Rfolder, "*.R"))
checkFiles += Rfiles
print("Found %i *.R file(s) in R/ subdirectory" % len(Rfiles))

# Find R documentation files in man/ subdirectory ----

manFolder = os.path.join(pkgDir, "man")

if not os.path.exists(manFolder):
    raise IOError("man/ subdirectory not found in %s" % manFolder)

if not os.path.isdir(manFolder):
    raise IOError(u"{0:s} is not a directory".format(manFolder))

manFiles = glob.glob(os.path.join(manFolder, "*.Rd"))
checkFiles += manFiles
print("Found %i *.Rd file(s) in man/ subdirectory" % len(manFiles))

# Find R vignette files in vignettes/ subdirectory ----

vignetteFolder = os.path.join(pkgDir, "vignettes")

if not os.path.exists(vignetteFolder):
    raise IOError("man/ subdirectory not found in %s" % vignetteFolder)

if not os.path.isdir(vignetteFolder):
    raise IOError("%s is not a directory" % vignetteFolder)

for extension in ["Rmd", "Rnw", "Rrst", "Rhtml", "Rtex"]:
    extension = "*.{0}".format(extension)
    vignetteFiles = glob.glob(os.path.join(vignetteFolder, extension))
    checkFiles += vignetteFiles
    if (len(vignetteFiles)):
        print("Found %i %s file(s) in vignettes/ subdirectory" % (len(vignetteFiles), extension))

print(checkFiles)
