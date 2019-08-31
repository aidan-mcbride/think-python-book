# exercises/6.3.2.py

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    # a one-letter word is a palindrome
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('racecar'))
print(is_palindrome('goldfish'))
print(is_palindrome('abcdba'))
print(is_palindrome('redivider'))
