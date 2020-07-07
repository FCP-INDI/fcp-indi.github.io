import os

from scripts.version_list import sort_versions

try:
    versions = os.listdir('docs')
    with open('build_version.txt') as bv:
        build_version = bv.read().strip()
    return(sort_versions(versions)[1] == build_version)
except:
    return(False)