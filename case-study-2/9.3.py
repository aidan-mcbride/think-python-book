fin = open('case-study-2/words.txt')

def avoids(word, forbidden):
    """
    takes a word as a string and a string of forbidden letters
    returns True if the word does not contain any forbidden letter
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

def avoid_list(word_list):
    """
    takes a list of words
    takes inputted list of forbidden characters
    returns a count of words not containing any forbidden characters
    """
    print("input string of forbidden letters:", end=" ")
    forbidden = input()

    word_count = 0
    for word in word_list:
        word = word.strip()
        if avoids(word, forbidden):
            word_count = word_count + 1

    print(str(word_count) + (" words contain no forbidden letters"))

print(avoids('racecar', 're'))
print(avoids('dynamo', 'yg'))

avoid_list(fin)
