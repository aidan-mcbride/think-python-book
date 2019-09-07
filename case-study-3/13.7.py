# case-study-3/13.7.py

import random, string
from bisect import bisect

def import_book(filename):
    """
    takes a book text file's filename
    opens that file
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


def random_word(hist):
    """
    takes a dict containing words and their frequencies(hist)
    Chooses a random word from that dict
    with probability proportional to frequency
    returns chosen word
    """

    words = list()
    freqs = list()
    total_freq = 0

    # make list of words, cumulative list of frequencies
    for word, freq in hist.items():
        words.append(word)
        total_freq += freq
        freqs.append(total_freq)

    # choose a random value, locate in cumulative list
    # https://docs.python.org/3.7/library/random.html
    # ---
    # USE BISECTION SORT:
    # https://docs.python.org/3.7/library/bisect.html
    r = random.randint(0, total_freq-1)
    index = bisect(freqs, r)
    return words[index]


#####################
#### RUN PROGRAM ####
#####################

emma = import_book("emma.txt")
book_words = parse_book(emma)
word_freq = word_frequency(book_words)

for i in range(20):
    print(random_word(word_freq))
