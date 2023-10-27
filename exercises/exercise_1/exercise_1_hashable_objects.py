def get_duplicates(l: list) -> list:
    frequencies = {}
    result = []

    for i in l:
        frequencies[i] = frequencies.get(i, 0) + 1

    for i in l:
        if frequencies[i] >= 2:
            result.append(i)
            frequencies[i] = 0
    return result


if __name__ == "__main__":
    print(get_duplicates(["a", "apple", "@", "B", "!", "9", "car", "apple", "X", "&", "a", "1", "B", "z", "9"]))
