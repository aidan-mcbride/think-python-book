# exercise/10.2.py

def cumsum(int_list):
    """
    takes a list of integers
    returns a list of integers that is the cumulative sum of the previous integers
    """
    new_list = []
    cum_sum = 0
    for num in int_list:
        cum_sum += num
        new_list.append(cum_sum)
    return new_list

t = [1, 2, 3]
print(cumsum(t))
