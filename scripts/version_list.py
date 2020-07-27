import os
import sys


def rewrite_versions(docs_path='/build/docs'):
    """
    Collects built versions and outputs a text file that lists 'latest', 
    latest version number, 'nightly', descending prior verions.
    """
    versions_txt_path = os.path.join(docs_path, 'versions.txt')
    with open(versions_txt_path, 'w') as vtp:
        vtp.write('\n'.join(sort_versions(os.listdir(docs_path))))
    

def sort_versions(versions):
    v2 = versions.copy()
    v2.sort(reverse=True)
    {v2.remove(v) for v in {
        'latest', 'nightly', '_sources', 'versions.txt'
    } if v in v2}
    if len(v2):
        if len(v2)<2:
            return(['latest', v2[0], 'nightly'])
        return(['latest', v2[0], 'nightly', *v2[1:]])
    return(['latest', 'nightly'])
    

if __name__ == '__main__':
    rewrite_versions(sys.argv[1]) if len(sys.argv) > 1 else rewrite_versions()