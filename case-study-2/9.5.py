fin = open('case-study-2/words.txt')

def uses_only(word, letters):
    """
    takes a word as a string and a string of letters
    returns True if the word contains only given letters
    """
    for letter in word:
        if letter not in letters:
            return False
    return True

def uses_all(word, letters):
    """
    takes a word as a string and a string of letters
    returns True if a word uses each letter at least once
    """
    # reverse params for uses_only:
    # required letter string uses only letters that are in word
    return uses_only(letters, word)

print(uses_all('racecar', 'race'))
print(uses_all('dynamo', 'yg'))
