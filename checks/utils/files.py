#!/usr/bin/python
# !/usr/bin/python2.7
# !/usr/bin/python3

import glob
import os


def listPackageFiles(path):
    """List files of R packages to check for guidelines"""
    print "\n  * Searching for files to check *\n"

    checkFiles = []

    # Add DESCRIPTION file to check list ----

    DESCRIPTIONfile = os.path.join(path, "DESCRIPTION")

    if not os.path.exists(DESCRIPTIONfile):
        raise IOError("DESCRIPTION file not found in %s" % path)

    checkFiles.append(DESCRIPTIONfile)

    # Add NAMESPACE file to check list ----

    NAMESPACEfile = os.path.join(path, "NAMESPACE")

    if not os.path.exists(NAMESPACEfile):
        raise IOError("NAMESPACE file not found in %s" % path)

    checkFiles.append(NAMESPACEfile)

    # Find *.R files in R/ subdirectory ----

    Rfolder = os.path.join(path, "R")

    if not os.path.exists(Rfolder):
        raise IOError("R/ subdirectory not found in %s" % Rfolder)

    if not os.path.isdir(Rfolder):
        raise IOError("%s is not a directory" % Rfolder)

    Rfiles = glob.glob(os.path.join(Rfolder, "*.R"))
    checkFiles += Rfiles
    print("Found %i *.R file(s) in R/ subdirectory" % len(Rfiles))

    # Find R documentation files in man/ subdirectory ----

    manFolder = os.path.join(path, "man")

    if not os.path.exists(manFolder):
        raise IOError("man/ subdirectory not found in %s" % manFolder)

    if not os.path.isdir(manFolder):
        raise IOError(u"{0:s} is not a directory".format(manFolder))

    manFiles = glob.glob(os.path.join(manFolder, "*.Rd"))
    checkFiles += manFiles
    print("Found %i *.Rd file(s) in man/ subdirectory" % len(manFiles))

    # Find R vignette files in vignettes/ subdirectory ----

    vignetteFolder = os.path.join(path, "vignettes")

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

    print ""
    return checkFiles
