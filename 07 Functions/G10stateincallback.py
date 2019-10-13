def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

def print_result(result):
    print('Got:', result)

class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

def make_handler():
    sequence = 0
    while True:
        sequence += 1
        result = yield
        print('[{}] Got: {}'.format(sequence, result))

if __name__ == '__main__':
    r = ResultHandler()
    apply_async(add, (1, 2), callback=r.handler)
    apply_async(add, ('hello', 'world'), callback=r.handler)

    handler = make_handler()
    next(handler)
    apply_async(add, (1, 2), callback=handler.send)
    apply_async(add, ('hello', 'world'), callback=handler.send)
