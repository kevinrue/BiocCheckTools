# BiocCheckTools
_Scripts to follow up on R CMD BiocCheck_

## Motivation

If you are familiar with any of the following messages when running
 `R CMD BiocCheck <dir>`:

```
* Checking formatting of DESCRIPTION, NAMESPACE, man pages, R source,
  and vignette source...
    * NOTE: Consider shorter lines; 1 lines (0%) are > 80 characters
      long.
    * NOTE: Consider 4 spaces instead of tabs; 4 lines (0%) contain tabs.
    * NOTE: Consider indenting lines with a multiple of 4 spaces; 1
      lines (0%) are not.
```

And you wish to rapidly find those problematic lines, then the
following scripts should be useful to you.

## Overview

My typical usage is, assuming the _Bioconductor_ package folder is
`/path/to/package` (relative paths work too):

```
BiocCheck.py /path/to/package
```

Alternatively, the individual modules may be called separately:

```
line_chars.py /path/to/package
tab_width.py /path/to/package
```

or in this way:

```
BiocCheck.py git/BiocCheck --mode line_chars
BiocCheck.py /path/to/package --mode tab_width
```

The output of the master/wrapper script looks like this (_truncated for readability_):

```
$ BiocCheck.py git/BiocCheck

  * Searching for files to check *

Found 5 *.R file(s) in R/ subdirectory
Found 1 *.Rd file(s) in man/ subdirectory
Found 1 *.Rmd file(s) in vignettes/ subdirectory

  * Searching for lines > 80 characters *

R/BiocCheck.R	(line 11)	92 chars
R/BiocCheck.R	(line 102)	86 chars
R/BiocCheck.R	(line 107)	90 chars
R/checks.R	(line 153)	109 chars
R/checks.R	(line 165)	82 chars
[... truncated for readability ...]
R/util.R	(line 126)	88 chars
R/util.R	(line 132)	81 chars
R/util.R	(line 217)	83 chars
vignettes/BiocCheck.Rmd	(line 159)	91 chars
vignettes/BiocCheck.Rmd	(line 268)	93 chars
vignettes/BiocCheck.Rmd	(line 397)	95 chars

=== Summary: 30 lines > 80 characters long. ===

  * Searching for lines not indented by a multiple of 4 spaces *

git/BiocCheck/DESCRIPTION	(line 12)	9 spaces
git/BiocCheck/DESCRIPTION	(line 14)	10 spaces
git/BiocCheck/R/checks.R	(line 241)	31 spaces
git/BiocCheck/R/checks.R	(line 1192)	13 spaces
git/BiocCheck/R/checks.R	(line 1194)	13 spaces
git/BiocCheck/R/util.R	(line 287)	7 spaces
git/BiocCheck/man/BiocCheck.Rd	(line 19)	2 spaces
git/BiocCheck/man/BiocCheck.Rd	(line 22)	2 spaces
git/BiocCheck/vignettes/BiocCheck.Rmd	(line 3)	2 spaces
[... truncated for readability ...]
git/BiocCheck/vignettes/BiocCheck.Rmd	(line 460)	2 spaces
git/BiocCheck/vignettes/BiocCheck.Rmd	(line 463)	2 spaces
git/BiocCheck/vignettes/BiocCheck.Rmd	(line 464)	2 spaces
git/BiocCheck/vignettes/BiocCheck.Rmd	(line 465)	2 spaces

=== Summary: 101 lines not indented by a multiple of 4 spaces. ===


=== Global summary ===
  30 lines > 80 characters long.
  101 lines not indented by multiple of 4 spaces.

```

## Installation

Clone the repository and add the folder on your `$PATH`:

```
git clone git@github.com:kevinrue/BiocCheckTools.git
export PATH=$PATH:$(pwd)/BiocCheckTools
```

## BiocCheck.py

### Purpose

Identify lines offending certain Bioconductor guidelines:

* lines > 80 characters
* lines not indented by multiple of 4 spaces

### Usage

```
usage: BiocCheck.py [-h] [--mode all] [--max_char 80] [--tab_width 4]
                    /path/to/package

Identify lines offending certain Bioconductor guidelines.

positional arguments:
  /path/to/package  Path to the package folder.

optional arguments:
  -h, --help        show this help message and exit
  --mode all        Modules to run. Choices: all, line_chars, tab_width.
  --max_char 80     The maximum number of characters allowed in a line.
  --tab_width 4     The number of spaces required in a tabulation.
```

## line_chars.py

### Purpose

Identify lines > N characters long.

The useful addition to the _Bioconductor_
[BiocCheck](https://bioconductor.org/packages/release/bioc/html/BiocCheck.html)
package is that each offending line is displayed along with the
corresponding filename and line number to rapidly find and correct it.

### Usage

```
usage: line_chars.py [-h] [--chars 80] /path/to/package

Identify lines > [chars] characters long.

positional arguments:
  /path/to/package  Path to the package folder.

optional arguments:
  -h, --help        show this help message and exit
  --chars 80        The maximum number of characters allowed in a line.
```

## tab_width.py

### Purpose

Identify lines not indented by a multiple of N spaces.

The useful addition to the _Bioconductor_
[BiocCheck](https://bioconductor.org/packages/release/bioc/html/BiocCheck.html)
package is that each offending line is displayed along with the
corresponding filename and line number to rapidly find and correct it.

### Usage

```
usage: tab_width.py [-h] [--width 4] /path/to/package

Identify lines not indented by a multiple of [width] spaces.

positional arguments:
  /path/to/package  Path to the package folder.

optional arguments:
  -h, --help        show this help message and exit
  --width 4         The number of spaces required in a tabulation.
```
