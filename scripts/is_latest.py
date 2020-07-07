import os
import sys

from version_list import sort_versions

versions = os.listdir('/build/docs')
with open('/build/build_version.txt') as bv:
    build_version = bv.read().strip()
if(sort_versions(versions)[1] == build_version):
    sys.exit(0)
sys.exit(1)