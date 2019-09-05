# exercises/12.1.py

def most_frequent(string):
    """
    takes a string
    prints the letters of that string in descending order
    of frequency
    returns nothing
    """
    # format string: remove spaces, make lower
    formatted = string.replace(' ', '').lower()

    # create dict of letters and frequency
    # based on `histogram()` from chapter 11
    hist = dict()
    for char in formatted:
        hist[char] = hist.get(char, 0) + 1

    # reverse keys and values with tuple assignment
    # hist.items() == list of each char and freq as tuples
    freq_list = list()
    for (char, freq) in hist.items():
        freq_list.append((freq, char))

    # sort frequency list
    # `reverse` sorts in descending order
    freq_list.sort(reverse=True)

    # create list of characters by frequency
    char_freq = list()
    for (freq, char) in freq_list:
        char_freq.append(char)

    print(char_freq)
