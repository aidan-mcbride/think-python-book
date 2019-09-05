# case-study-3/13.2.py


import string

def import_book(filename):
    """
    takes a book text file's filename
    returns the book as a string, sans the gutenberg header
    """
    with open('case-study-3/{}'.format(filename), 'r') as f:
        book_string = str()
        # book starts on line 34
        for i in range(33):
            next(f)
        for line in f:
            book_string += line

        # for testing, only return first 100 characters
        return book_string[:100]

plato = import_book('pg55201.txt')

print(plato)
