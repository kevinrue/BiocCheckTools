# BiocCheckTools
_Scripts to complement R CMD BiocCheck_

## Motivation

If you are familiar with any of the following messages when running `R CMD BiocCheck <dir>`:

```
* Checking formatting of DESCRIPTION, NAMESPACE, man pages, R source,
  and vignette source...
    * NOTE: Consider shorter lines; 1 lines (0%) are > 80 characters
      long.
    * NOTE: Consider indenting lines with a multiple of 4 spaces; 1
      lines (0%) are not.
```

And you wish to rapidly find those problematic lines, then those scripts are for you.

## Overview

My typical usage is, assuming the _Bioconductor_ package folder is `path/to/TVTB`

```
cd /path/to
listRpackage.sh TVTB > TVTBcheckFiles.txt
4spacetabs.py TVTBcheckFiles.txt
line_chars.py TVTBcheckFiles.txt
```

The output would then look like this:

```
$4spacetabs.py TVTBcheckFiles.txt
TVTB/man/TVTBParam-class.Rd:58: The \code{TVTBparam} class stores recurrent parameters of the \code{TVTB}zzzzzzz
1 lines not indented by a multiple of 4 spaces detected
```
and
```
# line_chars.py TVTBcheckFiles.txt
TVTB/man/TVTBParam-class.Rd:58: The \code{TVTBparam} class stores recurrent parameters of the \code{TVTB}zzzzzzz
1 lines over 80 characters long
```

## Installation

Clone the repository and add the folder on your `$PATH`:

```
git clone git@github.com:kevinrue/BiocCheckTools.git
export PATH=$PATH:$(pwd)
```

## listRpackage.sh

### Purpose

List all files checked by `R CMD BioCheck` in a file.

### Usage

```
listRfiles.sh pkgdir
```

### Notes

The script prints the filenames in the `stdout`, which must be redirected to a file.

## 4spacetabs.py

### Purpose

Print the lines that are not indented with a multiple of 4 spaces. The useful bit here is that each line is displayed along with the corresponding filename and line number to rapidly find and correct it.

### Usage

```
4spacetabs.py [-h] [--root rootFolder] listFiles.txt
```

## 4spacetabs.py

### Purpose

Print the lines that are > 80 characters long. The useful bit here is that each line is displayed along with the corresponding filename and line number to rapidly find and correct it.

### Usage

```
line_chars.py [-h] [--root rootFolder] [--max N] listFiles.txt
```
