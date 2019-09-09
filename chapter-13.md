# 13: Case Study: Data Structure Selection

## `13.1` Word Frequency Analysis

### `Exercise 13.1`

> Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.

```python
# case-study-3/13.1.1.py

import string

def parse(text):
    """
    takes a string of text
    splits text into words,
    removes whitespace and punctuation,
    and converts them to lowercase.
    """
    # remove punctuation
    no_punc = text.translate(text.maketrans('', '', string.punctuation))

    parsed = no_punc.lower().strip().split()
    return parsed

```

### `Exercise 13.2`

> Modify your program to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.
>
> Then modify the program to count the total number of words in the book, and the number of times each word is used.
>
> print the number of different words used in the book.

```python
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

```

### `Exercise 13.3`

> Modify the program from the previous exercise to print the 20 most frequently used words in the book.

```python
# case-study-3/13.3.py

# ...

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

```

### `Exercise 13.4`

> Modify the program to read a word list and then print all the words in the book that are not in the word list.

```python
# case-study-3/13.3.py

# ...

def import_word_list(filename):
    """
    takes a word list file's filename
    opens that file
    returns a list of the contents of the file
    """
    with open("case-study-3/{}".format(filename), "r") as f:
        wl = list()
        for line in f:
            wl.append(line.strip())
        return wl

#...

def not_in_list(book_words, word_list):
    """
    WARNING: TAKES FOREVER TO COMPLETE
    ---
    takes a list of all words in a book and a list of all known words
    returns a list of book words that are not in the list of all known words
    """
    not_in = list()

    for word in book_words:
        if word not in word_list:
            not_in.append(word)

    return not_in


#####################
#### RUN PROGRAM ####
#####################

plato = import_book("pg55201.txt")
word_list = import_word_list("words.txt")

book_words = parse_book(plato)
word_freq = word_frequency(book_words)
top_words = top_20(word_freq)

not_in = not_in_list(book_words, word_list)

for word in not_in:
    print(word)
```

---

## `13.2`

**Deterministic** programs will always generate the same output given the same input.

### `Exercise 13.5`

> Write a function named `choose_from_hist` that takes a histogram as defined in Section 11.2 and returns a random value from the histogram, chosen with probability in proportion to frequency.

*After thinking about this for a hot minute, the simplest solution I came up with was to convert the histogram back into the original list and then do `random.choice()` on that list. This seems wrong though since the first step in the example is to convert my list into a histogram, and I'm undoing that.*

```python
# case-study-3/13.5.py

import random

# from 11.2
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(hist):
    """
    takes a histogram
    returns a randomly selected key
    with probability based on value
    """
    p = list()
    for key, value in hist.items():
        for i in range(value):
            p.append(key)
    return random.choice(p)

t = ['a', 'a', 'b']
hist = histogram(t)

print(choose_from_hist(hist))

```

### `Exercise 13.6`

> Write a program that uses set subtraction to find words in the book that are not in the word list

*Modified from `13.4`*

```python
# case-study-3/13.6.py

# ...

def not_in_list(book_words, word_list):
    # ...
    return list(set(book_words) - set(word_list))

# ...

```

## `13.7`

* **Linear Search** - Iterate through a given list and, for each item, check if that item is the one we are looking for. Can be used on an unsorted list, but is very inefficient compared to...
* **Bisection/Binary Search**
  * Split a *<u>sorted</u>* list in half at some element
  * check if the element we are looking for would come *before* or *after* the element we selected from the list.
  * If before, split first half in half again.
  * If after, split the last half in half again.
  * Continue bisecting sections until we find the element we are looking for.

Bisection search can be implemented in python using the [`bisect` module](https://docs.python.org/3.7/library/bisect.html)

### `Exercise 13.7`

> Write a program that uses the bisection search algorithm to choose a random word from the book based on frequency.

```python
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

```

## `13.8`

**Markov analysis** takes a string of words and gives the probability that a certain word will be next in the sequence.

### `Exercise 13.8`

> Write a program to read text from a file and perform a Markov analysis. The result should be a dictionary that maps from prefixes to a collection of possible suffixes. You should write the program in a way that makes it easy to try other lengths of prefix.

```python
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

```

## `13.9` Data Structures

Choosing data structures:

* Supports intended operations 
* Ease of implementation
* Run time
* Memory usage

### `Exercise 13.9`

> Zipf's law
>
> **f = cr<sup>-s</sup>**
>
> ***log*f = *log*c - s*log*r**

> Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of frequency, with log f and log r.
>
> Use the graphing program of your choice to plot the results and check whether they form a straight line. Can you estimate the value of `s`?

