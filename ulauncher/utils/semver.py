# -*- coding:utf-8 -*-

# Extremely simplified semver just for Ulauncher-Revived's simple needs. It ignores
# ^ and ~, treats x as 0 and it only really checks that the Ulauncher-Revived version
# is higher or the same as the specified version, and the same major version.

def is_int(input):
    return isinstance(input, int)


def part_to_number(version_part):
    if version_part[0] in ["~", "^"]:
        version_part = version_part[1:]
    if version_part == "x":
        return 0
    if version_part.isnumeric():
        return int(version_part)
    return None


def get_version(version_string):
    match = list(filter(bool, (version_string + ".").split(".")))
    version = list(map(part_to_number, match))
    length = len(version)
    if length > 0 and length <= 3 and length == len(list(filter(is_int, version))):
        # pad to 3 digits
        return version + ([0] * (3 - len(version)))
    return None


def satisfies(version_string, expected_string):
    version = get_version(version_string)
    expected = get_version(expected_string)
    return version >= expected and version[0] == expected[0]


def valid_range(range):
    return bool(get_version(range))
