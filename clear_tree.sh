#!/bin/sh
set -e

for dir in */; do
    cd $dir
    rm -rf -- */
    rm -f PKGBUILD.stamp
    cd ..
done
