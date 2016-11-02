#!/bin/sh

usage="Usage:\n
\tlistRfiles.sh pkgdir"

if [ "$#" -ne 1 ]; then
    echo $usage
    exit 1
fi

pkgdir=$1; shift

find "$pkgdir/R" -name '*.R'
find "$pkgdir/man" -name '*.Rd'
find "$pkgdir/vignettes" -name '*.Rmd'
echo "$pkgdir/DESCRIPTION"
echo "$pkgdir/NAMESPACE"