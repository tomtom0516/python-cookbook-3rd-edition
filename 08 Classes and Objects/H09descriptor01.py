# Reference
#   https://blog.csdn.net/sjyttkl/article/details/80655421

# example

class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return 'get', self, instance, cls

    def __set__(self, instance, value):
        print('set', self, instance, value)

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('xx')
    y = Integer('yy')
    def __init__(self, x, y):
        self.x = x
        self.y = y


class T:
    name = 'name'
    def hello(self):
        print('hello')

def test():
    t = T()
    

if __name__ == "__main__":
    test()