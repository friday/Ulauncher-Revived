#!/usr/bin/env bash

##############################################################
# Builds tar.gz file with (un)install script and Ulauncher src
##############################################################
build-targz () {
    # Args:
    # $1 - version

    echo "###################################"
    echo "# Building ulauncher-$1.tar.gz"
    echo "###################################"

    set -ex

    ./ul build-preferences

    name="ulauncher"
    tmpdir="/tmp/$name"

    rm -rf $tmpdir || true
    mkdir -p $tmpdir || true
    rsync -aq --progress \
        AUTHORS \
        bin \
        data \
        LICENSE \
        README.md \
        setup.cfg \
        setup.py \
        ulauncher \
        ulauncher.desktop \
        $tmpdir \
        --exclude-from=.gitignore

    # This is only needed because data/preferences is in .gitignore
    cp -r data/preferences $tmpdir/data/preferences

    filename=$name
    if [ ! -z "$1" ]; then
        filename="${name}_$1"
    fi

    cd /tmp
    tar czf $filename.tar.gz $name
    rm -rf $tmpdir

    set +x

    echo
    echo "/tmp/$filename.tar.gz is built"
    echo
}
