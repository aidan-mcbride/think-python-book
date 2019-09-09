# case-study-3/13.9.py

"""
OUTLINE:

~~1. Import text file~~
~~2. Remove white space, punctuation, make lowercase~~
~~3. Turn into list of words~~
~~4. Create histogram of words and frequencies.~~
~~5. Sort histogram by frequency~~
6. For each word in sorted hist:
    - print word
    - print log f
    - print log r
7. Plot zipf's law
"""

import math, string
import matplotlib.pyplot as plt


def import_text(filename, start_line=0):
    """
    takes a text file's filename,
    and a start line.
    returns a string of the text in the file
    starting after the given start line
    """
    with open("case-study-3/{}".format(filename), "r") as f:
        text = str()
        for i in range(start_line):
            next(f)
        for line in f:
            text += line
        return text


def remove_punctuation(text):
    """
    takes a string
    returns the string without punctuation
    """
    return text.translate(text.maketrans("", "", string.punctuation))

def create_word_list(text):
    """
    takes a string of text
    splits string into words,
    removes whitespace,
    removes punctuation,
    converts all words to lowercase,
    then returns a list of words in their original sequence.
    """
    no_punc = remove_punctuation(text)
    parsed = no_punc.lower().strip()
    word_list = parsed.split()

    # FOR TESTING: return truncated list
    return word_list


def create_hist(word_list):
    """
    takes a list of words
    returns a dictionary where keys are words and values are frequencies
    """
    hist = dict()
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return hist

def sort_hist(hist):
    """
    takes a dict of words and their frequencies
    returns a sorted list of tuples, where each tuple is a word and its frequency (freq, word).
    """
    sorted = list()
    # reverse keys and values
    for word, freq in hist.items():
        sorted.append((freq, word))
    # sort in descending order
    sorted.sort(reverse=True)
    # return list of tuples where frequency comes before word
    # so we don't have to iterate through the list again
    # to reverse the keys and values again
    # since this is also done in the next step
    return sorted

def zipf_table(sorted_hist):
    """
    takes a list of tuples containing frequencies and words
    returns a list of tuples, where each tuple is:
    -   the word
    -   log of the word's rank
    -   log of the word's frequency
    """
    zipf = list()
    for i in range(len(sorted_hist)):
        freq, word = sorted_hist[i]
        logr = math.log(i+1)    # log rank of word
        logf = math.log(freq)   # log freq of word
        zipf.append((word, logr, logf))

    return zipf

def create_plot(zipf_table):
    """
    takes a list of tuples containing word, rank, and frequency
    generates a plot where logf is the x axis and logr is the y axis
    """
    x_data = list()
    y_data = list()
    for (word, logr, logf) in zipf_table:
        x_data.append(logr)
        y_data.append(logf)

    plt.plot(x_data, y_data)
    plt.show()


#####################
#### RUN PROGRAM ####
#####################
emma = import_text('emma.txt', 248)
word_list = create_word_list(emma)
hist = create_hist(word_list)
sorted = sort_hist(hist)
zipf = zipf_table(sorted)

create_plot(zipf)
