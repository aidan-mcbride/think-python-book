# case-study-3/13.1.py

sample_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."


import string

def parse(text):
    """
    takes a string of text
    splits text into words,
    removes whitespace and punctuation,
    and converts them to lowercase.
    """
    # remove punctuation
    no_punc = text.translate(text.maketrans('', '', string.punctuation))

    parsed = no_punc.lower().strip().split()
    return parsed

print(parse(sample_text))
