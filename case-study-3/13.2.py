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

        # for testing, only return first 200 characters
        return book_string[:200]

def parse_book(text):
    """
    takes an entire book as as single string
    splits string into words,
    removes whitespace and punctuation,
    and converts all words to lowercase.
    returns a list of words
    """
    # remove punctuation
    no_punc = text.translate(text.maketrans('', '', string.punctuation))

    parsed = no_punc.lower().strip().split()
    return parsed


plato = import_book('pg55201.txt')

print(parse_book(plato))
