def dedupe(items):
    seen = set()
    for item in items:
        sorted_item = dict(sorted(item.items()))
        keys = tuple(sorted_item.keys())
        values = tuple(sorted_item.values())
        val = (keys, values)
        if val not in seen:
            print(val)
            yield item
            seen.add(val)


def test():
    input_ = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'y':2, 'x':1}, {'x':2, 'y':4}]
    output = list(dedupe(input_))
    print(output)


if __name__ == "__main__":
    test()