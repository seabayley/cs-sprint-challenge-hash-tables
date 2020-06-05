# Your code here


def finder(files, queries):
    # return [x for x in files for y in queries if y in x] # For short lists.
    c = {}
    results = []
    for f in files:
        c.setdefault(f.rsplit('/')[-1], []).append(f)

    for q in queries:
        if q in c.keys():
            for fn in c[q]:
                results.append(fn)
    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
