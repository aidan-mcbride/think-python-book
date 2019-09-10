# exercises/14.2.py

import os, shelve

import anagram_sets

def store_anagrams(filepath):
    """
    creates dictionary of anagrams in a list of words
    in a given file at filepath
    stores dictionary in a 'shelf'
    """
    # extract filename from given path
    # for use as shelf file name
    filename = os.path.splitext(filepath)[0]
    anagrams = anagram_sets.all_anagrams(filepath)
    print(anagrams)
    try:
        with shelve.open(filename) as db:
            for key, value in anagrams.items():
                db[key] = value
    except:
        print('error writing to shelf')

def read_anagrams(database, word):
    """
    looks up a given word in a given database
    returns a list of of anagrams for that word
    """
    try:
        with shelve.open(database) as db:
            return db[word]
    except:
        print('error reading from shelf')


# run program
if __name__ == '__main__':
    store_anagrams('exercises/test.txt')
    print(read_anagrams('exercises/test', 'glo'))
