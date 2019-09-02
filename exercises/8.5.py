# exercises/8.5.py

def rotate_letter(letter, amount):
    if letter.isupper():
        start_code = ord('A')
    elif letter.islower():
        start_code = ord('a')
    else:
        # if 'letter' is not a letter, don't rotate
        return letter

    # rotate letter *within* range of alphabet
    letter_code = ord(letter) - start_code
    # '%' will return operand if under 26
    # or operand - 26 if over 26
    new_letter_code = (letter_code + amount) % 26 + start_code
    return chr(new_letter_code)

def rotate_word(word, amount=0):
    rv = ''
    for letter in word:
        rv = rv + rotate_letter(letter, amount)
    return rv

# tests from solution in book
print(rotate_word('cheer!', 7))
print(rotate_word('melon', -10))
print(rotate_word('Sleep', 9))
