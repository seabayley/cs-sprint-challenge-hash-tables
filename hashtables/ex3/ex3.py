def intersection(arrays):
    c = {}
    result = []
    for a in arrays:
        for i in a:
            c[i] = c[i] + 1 if i in c else 1

    return [k for (k, v) in c.items() if v == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
