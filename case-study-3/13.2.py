# case-study-3/13.2.py


import string


def import_book(filename):
    """
    takes a book text file's filename
    returns the book as a string, sans the gutenberg header
    """
    with open("case-study-3/{}".format(filename), "r") as f:
        book_string = str()
        # book starts on line 34
        for i in range(33):
            next(f)
        for line in f:
            book_string += line

        # for testing, only return first 300 words
        return book_string[:300]


def parse_book(text):
    """
    takes an entire book as as single string
    splits string into words,
    removes whitespace and punctuation,
    and converts all words to lowercase.
    returns a list of words
    """
    # remove punctuation
    no_punc = text.translate(text.maketrans("", "", string.punctuation))

    parsed = no_punc.lower().strip().split()
    return parsed


def word_frequency(word_list):
    """
    takes a list of words
    creates a dictionary where the key is a word
    and the value is the frequency of that word
    returns that dictionary
    """
    # histogram function basically
    hist = dict()
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return hist


#####################
#### RUN PROGRAM ####
#####################

plato = import_book("pg55201.txt")

word_list = parse_book(plato)
word_freq = word_frequency(word_list)

print("total words: {}".format(len(word_list)))
print(word_freq)
print("different words: {}".format(len(word_freq)))
