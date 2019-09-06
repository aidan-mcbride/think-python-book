# case-study-3/13.3.py


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

        return book_string


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


def top_20(word_freq):
    """
    takes a dictionary of words and how many times they occur
    returns a list of the 20 most frequent words
    """
    # based on  12.1
    fr = list()
    # reverse keys and values
    for word, freq in word_freq.items():
        fr.append((freq, word))
    # sort new list
    fr.sort(reverse=True)
    # create list of most frequent words

    mf = list()
    for (freq, word) in fr:
        mf.append(word)

    # only return top 20
    return mf[:20]


#####################
#### RUN PROGRAM ####
#####################

plato = import_book("pg55201.txt")

word_list = parse_book(plato)
word_freq = word_frequency(word_list)
top_words = top_20(word_freq)

for word in top_words:
    print(word)
