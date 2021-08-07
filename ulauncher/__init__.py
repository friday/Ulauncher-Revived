from os import path

# This file is overwritten by the build_wrapper script in setup.py
# IF YOU EDIT THIS FILE make sure your changes are reflected there

__data_directory__ = path.realpath(path.join(path.dirname(__file__), "../data/"))
__version__ = open("ulauncher/VERSION").read().strip()
__is_dev__ = True
