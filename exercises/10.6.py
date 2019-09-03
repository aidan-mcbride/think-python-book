# exercises/10.6.py

def is_anagram(s1, s2):
    """
    takes two strings
    returns True if s1 is an anagram of s2
    """
    s1 = list(s1.replace(' ', ''))
    s2 = list(s2.replace(' ', ''))
    s1.sort()
    s2.sort()
    return s1 == s2

# anagrams from:
# https://literarydevices.net/anagram/
print(is_anagram('debit card', 'bad credit'))
print(is_anagram('racecar', 'dynamo'))
