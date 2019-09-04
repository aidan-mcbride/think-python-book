# exercises/11.1.py

fin = open('exercises/words.txt')

words = dict()

def words_to_dict(word_list):
    """
    takes a list of words
    creates a dictionary with each word as a key
    with a value of 0
    """
    for word in word_list:
        word = word.strip()
        words[word] = 0

words_to_dict(fin)
