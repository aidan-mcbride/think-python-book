fin = open('case-study-2/words.txt')

def has_no_e(word):
    """
    takes a word as a string
    returns True if the word does not contain the letter 'e'
    """
    for letter in word:
        if letter == 'e':
            return False
    return True

def no_e_list(word_list):
    word_count = 0
    e_count = 0
    for word in word_list:
        word = word.strip()
        word_count = word_count + 1
        if has_no_e(word):
            print(word)
            e_count = e_count + 1

    e_percent = int((e_count / word_count) * 100)
    print(str(e_percent) + "% of words do not contain the letter 'e'")

print(has_no_e('racecar'))
print(has_no_e('dynamo'))

no_e_list(fin)
