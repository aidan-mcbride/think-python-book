# exercises/14.3.2.py

import hashlib, os

md5_map = dict()

def create_md5_map(dir, ext=None):
    """
    walks through a given directory and all subdirs
    maps md5 checksums to the paths to files with those checksums
    """
    global md5_map
    for root, dirs, files in os.walk(dir):
        for file in files:
            if ext == None or os.path.splitext(file)[1] == ext:
                # add to dict checksum: [filename, filename]
                path = os.path.abspath(file)
                md5 = create_checksum(file)
                md5_map[md5] = md5_map.get(md5, [])
                md5_map[md5].append(path)

def create_checksum(file):
    """
    takes a file
    returns a checksum for that file
    """
    return hashlib.md5(file.encode('utf-8')).hexdigest()

if __name__=="__main__":
    walk('.', '.txt')
    for key, value in md5_map.items():
        print("{}\t{}".format(key, value))
