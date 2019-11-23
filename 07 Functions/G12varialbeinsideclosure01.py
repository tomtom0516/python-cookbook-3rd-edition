def example():
    n = 0
    def func():
        print('n =', n)
    
    def get_n():
        return n

    def set_n(x):
        nonlocal n
        n = x

    func.get_n = get_n
    func.set_n = set_n

    return func

def test():
    f = example()
    f()
    f.set_n(10)
    f()
    print(f.get_n())
    
if __name__ == "__main__":
    test()
