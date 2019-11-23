# PyFrameObject

import sys

class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
            print(locals.keys())
        self.__dict__.update((key, value) for key, value in locals.items())
    
    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


def test():
    s = Stack()
    print(s)
    s.push(10)
    s.push(20)
    s.push('Hello')
    print(len(s))
    print(s.pop())


if __name__ == "__main__":
    test()