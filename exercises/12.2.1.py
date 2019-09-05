# exercises/12.2.1.py

fin = open("exercises/words.txt")


def word_to_tuple(word):
    """
    takes a word
    returns a tuple of each letter in that word
    sorted alphabetically
    """
    # since strings are sequences of letters
    # `sorted` will automatically convert a string
    # to a list, then sort it
    word = tuple(sorted(word))
    return word


def print_anagrams(anagrams):
    """
    takes a dictionary of lists of words keyed
    to tuples of the letters in those words
    prints any list of words with more than one word in it.
    """
    for letter_set in anagrams:
        words = anagrams.get(letter_set)
        if len(words) > 1:
            print(words)


def anagrams(word_list):
    """
    takes a list of words
    returns a dictionary containing lists of words
    keyed to tuples of the letters in those words
    """
    output = dict()

    for word in word_list:
        word = word.strip()
        letters = word_to_tuple(word)
        # add letters as key to output dict
        # if not present already
        output[letters] = output.get(letters, [])
        # append word to list at key
        output[letters].append(word)

    return output


print_anagrams(anagrams(fin))
