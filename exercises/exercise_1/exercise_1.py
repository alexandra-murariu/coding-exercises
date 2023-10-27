def get_duplicates(lst: list) -> list:
    """
    This function returns a list of duplicate elements in a given list.

    :param lst: The input list (can contain any type of objects).
    :type lst: list
    :returns: A list containing duplicate elements ("duplicate" in this case refers to "is" equality).
    :rtype: list
        """
    appeared = []
    lst = [x for x in lst if any(x is y for y in appeared) or appeared.append(x)]
    return lst
