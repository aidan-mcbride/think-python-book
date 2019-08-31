# exercises/palindrome.py

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


# tests
print(first('cat')) # c
print(first('x'))   # x
print(first(''))    # IndexError: string index out of range

print(last('cat'))  # t
print(last('x'))    # x
print(last(''))     # IndexError: string index out of range

print(middle('cat'))    # a
print(middle('xy'))     # ''
print(middle('x'))      # ''
print(middle(''))       # ''
