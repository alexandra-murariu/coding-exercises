def get_duplicates(lst: list, comparator=lambda x, y: x == y) -> list:
    """
    This function returns a list of duplicate elements in a given list. It is compatible with hashable or non-hashable
    elements in the input, as long as the object type does have the comparator definition.

    It is not as efficient as the only-hashable objects solution (which is displayed in module
    exercise_1_hashable_objects.py). In here, any new item is added to the appeared list. If it is already present in
    the appeared list, we should see if it is present in the result list. If not, the element is added to the result
    list.

    :param lst: The input list (can contain any type of objects).
    :type lst: list
    :param comparator: The equality of duplicates operator (could be '==', or 'is', or any other comparator)
    :type comparator: function
    :returns: A list containing duplicate elements ("duplicate" in this case refers to the comparator defined equality).
    :rtype: list
    """
    appeared = []
    result = []
    for x in lst:
        if any(comparator(x, y) for y in appeared):
            if x not in result:
                result.append(x)
        else:
            appeared.append(x)
    return result
