# exercises/14.1.py

def sed(filename1, filename2, pattern='', replace=''):
    """
    filename1:  file to copy from
    filename2:  file to copy to
    pattern:    string to be replaced
    replace:    string to replace pattern with
    """
    # see here for text IO methods:
    # https://docs.python.org/3.7/library/io.html#io.TextIOBase.read
    try:
        fin = open(filename1, 'r').read().replace(pattern, replace)
        fout = open(filename2, 'w')
        fout.write(fin)
    except:
        print("Error occurred while copying file")
