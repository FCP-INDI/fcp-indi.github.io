"""This script takes a version string as a commandline argument and updates
the links in `docs/{version}` that point to code in the `master` branch of
FCP-INDI/C-PAC to code in the tagged version.

Usage
-----
python link_to_set_version.py $VERSION
"""

import os
import sys

from glob import glob


def set_version(version):
    # Look for links to master branch
    patterns = [
        'FCP-INDI/C-PAC/blob/master',
        'FCP-INDI/C-PAC/master'
    ]
    for filepath in glob('/'.join([
        'docs', version, '**'
    ]), recursive=True):
        if 'release_notes' not in filepath and os.path.isfile(filepath):
            try:
                # Replace links to master branch with links to specified branch
                with open(filepath, 'r') as openfile:
                    file = openfile.read().replace(
                        patterns[0], 'FCP-INDI/C-PAC/blob/{}'.format(version)
                    ).replace(
                        patterns[1], 'FCP-INDI/C-PAC/{}'.format(version)
                    )
                with open(filepath, 'w') as openfile:
                    openfile.write(file)
            except UnicodeDecodeError:
                # List files that could not be opened to do find-and-replace
                print(' '.join([
                    'Couldn\'t find and replace in file', filepath
                ]))


if __name__ == '__main__':
    if sys.argv[1] not in {'latest', 'nightly', 'develop'}:
        set_version(sys.argv[1])
