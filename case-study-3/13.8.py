# case-study-3/13.8.py

import random, string

def import_book(filename, start_line):
    """
    takes a book text file's filename
    takes the start line, all lines before it are skipped
    opens that file
    returns the book as a string, sans the gutenberg header
    """
    with open("case-study-3/{}".format(filename), "r") as f:
        book_string = str()
        for i in range(start_line):
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

    # FOR TESTING: return truncated list
    return parsed

def create_markov_map(word_list, prefix_length=2):
    """
    takes a list of words and a length for prefixes
    creates a dictionary where the keys are prefixes as tuples
    and the values are lists of words following those prefixes
    returns this dict
    """
    markov_map = dict()
    current_prefix = tuple()
    for word in word_list:
        if len(current_prefix) == prefix_length:
            markov_map[current_prefix] = markov_map.get(current_prefix, [])
            markov_map[current_prefix].append(word)
            current_prefix = current_prefix[1:] + (word,)
        else:
            # if prefix is too short, just add word
            current_prefix += word,
    return markov_map


def create_markov_chain(map, length=100):
    """
    takes a markov mapping, and a length
    returns a string of words of the given length
    that is generated from the markov map
    """
    markov_chain = str()
    # start with a random prefix
    seed = random.choice(list(markov_map.keys()))

    for i in range(length):
        suffixes = markov_map.get(seed, None)
        word = random.choice(suffixes)
        markov_chain += word + " "
        seed = seed[1:] + (word,)

    return markov_chain


#####################
#### RUN PROGRAM ####
#####################

emma = import_book("emma.txt", 248)
book_words = parse_book(emma)

markov_map = create_markov_map(book_words, 4)

print(create_markov_chain(markov_map))
