fin = open('case-study-2/words.txt')

def is_abecedarian(word):
    """
    takes a word as a string
    returns True if letters in a word are in alphabetical order
    """
    # track previous letter, start with first letter
    previous_letter = word[0]
    for letter in word:
        # compare previous letter to current letter
        if letter < previous_letter:
            return False
        previous_letter = letter
    return True

print(is_abecedarian("apple"))
print(is_abecedarian("abby"))


def is_abecedarian_list(word_list):
    """
    takes a list of words
    returns a count of how many words are abecedarian
    """
    counter = 0
    for word in word_list:
        word = word.strip()
        if is_abecedarian(word):
            counter = counter + 1
    return counter

print(is_abecedarian_list(fin))
