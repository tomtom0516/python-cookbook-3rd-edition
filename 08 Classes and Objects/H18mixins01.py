class LogMixin:
    __slot__ = ()

    def __getitem__(self, key):
        print('Getting', str(key))
        return super().__getitem__(key)


class MyDict(LogMixin, dict):
    pass


def test():
    d = MyDict()
    d['x'] = 1
    print(d['x'])

if __name__ == "__main__":
    test()