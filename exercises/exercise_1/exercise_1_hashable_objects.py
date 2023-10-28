def get_duplicates(lst: list) -> list:
    """
    This function returns a list of duplicate elements in a given list. It is compatible only with hashable
    elements in the input.

    This solution is more efficient than the previous one, because it uses a dictionary, whose keys (objects) are stored
    inside a hashmap. Thus, key lookup is on average O(1).
    :param lst: the input list of hashable elements
    :type lst: list
    :return: the duplicates list
    :rtype: list
    """
    frequencies = {}
    result = []

    for i in lst:
        frequencies[i] = frequencies.get(i, 0) + 1

    for i in lst:
        if frequencies[i] >= 2:
            result.append(i)
            frequencies[i] = 0
    return result
