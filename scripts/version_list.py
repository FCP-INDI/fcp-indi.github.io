import os
from pathlib import Path
import sys


def rewrite_versions(docs_path='/build/docs'):
    """
    Collects built versions and outputs a text file that lists 'latest',
    latest version number, 'nightly', descending prior verions.
    """
    docs_path = Path(docs_path)
    versions_txt_path = docs_path.joinpath('versions.txt')
    versions_urls_path = docs_path.joinpath('versions_urls.txt')
    versions = sort_versions(os.listdir(docs_path))
    with versions_txt_path.open("w") as vtp:
        vtp.write('\n'.join(versions))
    with versions_urls_path.open("w") as vup:
        vup.write('\n'.join([f'https://fcp-indi.github.io/docs/{v}' for v in versions]))
    


def sort_versions(versions):
    v2 = versions.copy()
    v2.sort(reverse=True)
    {v2.remove(v) for v in {
        'latest', 'nightly', '_sources', 'versions.txt'
    } if v in v2}
    if len(v2):
        if len(v2) < 2:
            return(['latest', v2[0], 'nightly'])
        return(['latest', v2[0], 'nightly'] + v2[1:])
    return(['latest', 'nightly'])


if __name__ == '__main__':
    rewrite_versions(sys.argv[1]) if len(sys.argv) > 1 else rewrite_versions()
