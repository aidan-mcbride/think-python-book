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
