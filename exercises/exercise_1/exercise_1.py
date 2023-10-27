def get_duplicates(lst: list) -> list:
    appeared = []
    lst = [x for x in lst if any(x is y for y in appeared) or appeared.append(x)]
    return lst


if __name__ == "__main__":
    l = [1, 2]
    print(get_duplicates(["b", 1, 2, "a", 3, (1, 2), l, "b", (1, 2), l, 3.0, 4.0, 3, "a"]))
    print(get_duplicates(["b", 1, 2, "a", 3, (1, 2), [1, 2], "b", (1, 2), [1, 2], 3.0, 4.0, 3, "a"]))
