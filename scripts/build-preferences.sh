#!/usr/bin/env bash

#############################################
# Builds Ulauncher Preferences UI with nodejs
#############################################
build-preferences () {
    set -e
    NEWEST_SRC_FILE=$(ls -t preferences-src/**/* | head -n1)
    if [[ $NEWEST_SRC_FILE -ot data/preferences ]]; then
        echo "Detected no changes to Preferences since last build."
        return
    fi

    echo "Building Preferences."
    cd preferences-src

    set -x
    yarn install
    yarn lint
    yarn unit
    yarn build
}
