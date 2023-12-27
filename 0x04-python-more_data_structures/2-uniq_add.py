def uniq_add(my_list=[]):
    """
    This function takes a list and returns a list with the duplicates removed.
    """
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
