# exercises/14.3.1.py

import os

def walk(dir, ext=None):
    """
    walks through a given directory and all subdirs
    returns the abspath for any files with the given extension
    if no ext given, returns all files
    """
    for root, dirs, files in os.walk(dir):
        for file in files:
            if ext == None or os.path.splitext(file)[1] == ext:
                print(os.path.abspath(file))

if __name__=="__main__":
    walk('.', '.txt')
