def get_duplicates(lst: list) -> list:
    frequencies = {}
    result = []

    for i in lst:
        frequencies[i] = frequencies.get(i, 0) + 1

    for i in lst:
        if frequencies[i] >= 2:
            result.append(i)
            frequencies[i] = 0
    return result
