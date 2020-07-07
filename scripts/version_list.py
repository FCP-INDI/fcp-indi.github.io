import os


def rewrite_versions():
    """
    Collects built versions and outputs a text file that lists 'latest', 
    latest version number, 'develop', descending prior verions.
    """
    versions_txt_path = '/build/docs/versions.txt'
    with open(versions_txt_path, 'w') as vtp:
        vtp.write('\n'.join(sort_versions(os.listdir('/build/docs'))))
    

def sort_versions(versions):
    v2 = versions.copy()
    v2.sort(reverse=True)
    {v2.remove(v) for v in {
        'latest', 'develop', '_sources', 'versions.txt'
    } if v in v2}
    if len(v2):
        if len(v2)<2:
            return(['latest', v2[0], 'develop'])
        return(['latest', v2[0], 'develop', *v2[1:]])
    return(['latest', 'develop'])
    

if __name__ == '__main__':
    rewrite_versions()