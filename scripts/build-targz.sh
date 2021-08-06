#!/usr/bin/env bash

##############################################################
# Builds tar.gz file with (un)install script and Ulauncher src
##############################################################
build-targz () {
    version=$(<ulauncher/VERSION)
    name="ulauncher"
    tmpdir="/tmp/$name"

    echo "###################################"
    echo "# Building ulauncher-$version.tar.gz"
    echo "###################################"

    set -ex
    ./ul build-preferences

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
        ulauncher.service \
        $tmpdir \
        --exclude-from=.gitignore

    # This is only needed because data/preferences is in .gitignore
    cp -r data/preferences $tmpdir/data/preferences

    filename=$name
    if [ ! -z "$version" ]; then
        filename="${name}_$version"
    fi

    cd /tmp
    tar czf $filename.tar.gz $name
    rm -rf $tmpdir

    set +x

    echo
    echo "/tmp/$filename.tar.gz is built"
    echo
}
