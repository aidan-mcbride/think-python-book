# exercises/14.3.3.py

import hashlib, os

def walk(dir):
    """
    returns a list of all files in a directory and its subdirectories.
    Files are represented by absolute paths

    dir: string name of directory to walk
    """
    file_list = list()
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.abspath(file)
            file_list.append(path)
    return file_list

def create_checksum(file):
    """
    returns an md5 checksum for a given file
    """
    return hashlib.md5(file.encode('utf-8')).hexdigest()

def create_checksum_map(dir, ext=None):
    """
    create a mapping of checksums to matching
    files with the given extension in a given
    directory and its subdirectories.

    return mapping as dict
    """
    map = dict()
    files = walk(dir)
    for file in files:
        if ext==None or os.path.splitext(file)[1]==ext:
            checksum = create_checksum(file)
            map[checksum] = map.get(checksum, [])
            map[checksum].append(file)
    return map


def check_diff(file1, file2):
    """
    computes the difference between the contents of two files
    """
    cmd = "diff {} {}".format(file1, file2)
    pipe = os.popen(cmd)
    rv = pipe.read()
    return rv

def list_diff(list):
    """
    checks whether any files in a list differ from the others.

    returns False if no diff found,
    returns True if any diff found.
    """
    for filename1 in list:
        for filename2 in list:
            if filename1 < filename2:
                diff = check_diff(filename1, filename2)
                if diff == True:
                    return True
    return False

def print_duplicates(md5_map):
    """
    takes a mapping of checksums to matching files
    prints any files with the same checksum
    prints whether the files are identical
    """
    for key, files in md5_map.items():
        if len(files) > 1:
            print('same checksum:')
            for file in files:
                print(file)

            if list_diff(files):
                print('differences found!')
            else:
                print('no differences found: files are identical')


if __name__=="__main__":
    md5_map = create_checksum_map(dir='.', ext=".txt")
    print_duplicates(md5_map)
