def frange(start, stop, step):
    v = start
    while v < stop:
        yield v
        v += step


def test():
    gen = frange(0, 10, 0.5)
    for i in gen:
        print(i)
    print(list(frange(1, 4.5, 0.125)))


if __name__ == "__main__":
    test()
