def nested_sum(int_list):
    """
    takes a list of lists of integers
    returns the sum of all integers in all lists
    """
    total = 0
    for sub_list in int_list:
        total += sum(sub_list)
    return total
