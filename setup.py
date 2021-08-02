#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

import os
import subprocess
import sys
from glob import glob
from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
from ulauncher import __version__


def data_files_from_path(package_path, real_path):
    # Creates a list of valid entries for data_files weird custom format
    # Recurses over the real_path and adds it's content to package_path
    entries = []
    for file in list(glob(real_path + "/**/*", recursive=True)):
        if os.path.isfile(file):
            [dir, name] = os.path.split(file)
            entries.append((dir.replace(real_path, package_path), [dir + "/" + name]))
    return entries


class build_wrapper(build_py):
    def run(self):
        # Build Preferences before python package build
        subprocess.run(["./ul", "build-preferences"], check=True)
        build_py.run(self)
        print("Overwriting the namespace package with fixed values")
        namespace_package = os.path.realpath(os.path.join(self.build_lib, "ulauncher/__init__.py"))
        file = open(namespace_package, "w")
        file.write("\n".join([
            "__data_directory__ = '%s'" % os.path.join(sys.prefix, "share/ulauncher"),
            "__version__ = '%s'" % __version__
        ]))
        file.close()


setup(
    packages=find_packages(exclude=["tests"]),
    # These will be placed in /usr
    data_files=[
        ("share/applications", ["ulauncher.desktop"]),
        ("lib/systemd/user", ["contrib/systemd/ulauncher.service"]),
        ("share/doc/ulauncher", ["README.md"]),
        ("share/licenses/ulauncher", ["LICENSE"]),
        # Install icons in themes, so different icons can be used for different depending on theme
        # It's only needed for the app indicator icon
        ("share/icons/hicolor/48x48/apps", ["data/icons/system/default/ulauncher-indicator.svg"]),
        ("share/icons/hicolor/scalable/apps", ["data/icons/system/default/ulauncher-indicator.svg"]),
        # for Fedora + GNOME
        ("share/icons/gnome/scalable/apps", ["data/icons/system/default/ulauncher-indicator.svg"]),
        # for Elementary
        ("share/icons/elementary/scalable/apps", ["data/icons/system/light/ulauncher-indicator.svg"]),
        # for Ubuntu
        ("share/icons/breeze/apps/48", ["data/icons/system/dark/ulauncher-indicator.svg"]),
        ("share/icons/ubuntu-mono-dark/scalable/apps", ["data/icons/system/default/ulauncher-indicator.svg"]),
        ("share/icons/ubuntu-mono-light/scalable/apps", ["data/icons/system/dark/ulauncher-indicator.svg"]),
        # Recursively add data as share/ulauncher
        *data_files_from_path("share/ulauncher", "data"),
    ],
    cmdclass={'build_py': build_wrapper}
)
