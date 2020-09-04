import os
import sys

from version_list import sort_versions


docs_dir = sys.argv[1] if len(sys.argv) > 1 else '/build/docs'
versions = os.listdir(docs_dir)
with open('/build/build_version.txt') as bv:
    build_version = bv.read().strip()
if(sort_versions(versions)[1] == build_version):
    sys.exit(0)
sys.exit(1)