# exercises/12.2.1.py

"""
File reader -> word list

output_dict = {
    ('a', 'b', 'c'): ['abc', 'cab',' bac', 'cba'],
}

for each word in word list:
    create list of letters in word, sorted, INCLUDING DUPES
    if this set of letters is already a key in output_dict:
        add this word to the list for that key
    else:
        add these letters as a key, add this word to a list as a value
---
refine:
---
for each word in word list:
    create a tuple of the letters in the word, sorted
    see if this is an existing key in output_dict
        if not: add as key with an empty list as a value
    append the word to the list for that key
"""

# fin = open('exercises/words.txt')

### TESTING ###
fin = ['cat', 'rat', 'art', 'tack']

def word_to_tuple(word):
    """
    takes a word
    returns a tuple of each letter in that word
    sorted alphabetically
    """
    word = word.strip()
    # since strings are sequences of letters
    # `sorted` will automatically convert a string
    # to a list, then sort it
    word = tuple(sorted(word))
    return word


def anagrams(word_list):
    output = dict()

    for word in word_list:
        letters = word_to_tuple(word)
        # add letters as key to output dict
        # if not present already
        output[letters] = output.get(letters, [])
        # append word to list at key
        output[letters].append(word)

    print(output)

#### TEST ####
anagrams(fin)
