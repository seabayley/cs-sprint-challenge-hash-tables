def has_negatives(a):
    c = {}
    for i in sorted(a, reverse=True):
        c[abs(i)] = False if i > 0 else True if abs(i) in c else False

    return [k for (k, v) in c.items() if v == True]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
