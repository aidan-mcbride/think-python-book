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


print(uses_only('racecar', 'race'))
print(uses_only('dynamo', 'yg'))
