# 13: Case Study: Data Structure Selection

## `13.1` Word Frequency Analysis

### `Exercise 13.1.1`

> Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.

```python
# case-study-3/13.1.1.py

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

```

