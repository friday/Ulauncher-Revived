#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

import subprocess
import sys
from pathlib import Path
from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
from ulauncher import __version__


def data_files_from_path(target_path, source_path):
    # Creates a list of valid entries for data_files weird custom format
    # Recurses over the real_path and adds it's content to package_path
    entries = []
    for p in Path.cwd().glob(source_path + '/**/*'):
        if p.is_file():
            relative_file = p.relative_to(Path(source_path).absolute())
            entries.append((
                f'{target_path}/{relative_file.parent}',
                [f'{source_path}/{relative_file}'])
            )
    return entries


class build_wrapper(build_py):
    def run(self):
        # Build Preferences before python package build
        subprocess.run(["./ul", "build-preferences"], check=True)
        build_py.run(self)
        print("Overwriting the namespace package with fixed values")
        Path(self.build_lib + "/ulauncher/__init__.py").write_text("\n".join([
            "__data_directory__ = '%s/share/ulauncher'" % sys.prefix,
            "__version__ = '%s'" % __version__
        ]))


setup(
    packages=find_packages(exclude=["tests"]),
    # These will be placed in /usr
    data_files=[
        ("share/applications", ["ulauncher.desktop"]),
        ("lib/systemd/user", ["ulauncher.service"]),
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
