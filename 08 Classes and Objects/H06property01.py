class Person:

    def __init__(self, name):
        print('I am __init__()', name)
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self, name):
        if not isinstance(name, str):
            raise Exception('Name must be string')
        self._name = name
    

def test():
    p = Person('yapeng')
    print(p.name)
    p.name = 10
    print(p.name)


if __name__ == "__main__":
    test()
