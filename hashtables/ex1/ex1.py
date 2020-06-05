def get_indices_of_item_weights(weights, length, limit):
    c = {}
    for i, v in enumerate(weights):
        if v in c and v*2 == limit:
            return i, c[v]
        else:
            c[v] = i
    for i in c:
        if limit - i in c:
            return sorted([c[i], c[limit-i]], reverse=True)
