from collections import namedtuple
s = namedtuple('Nation', ['code', 'name'])
stock1 = s('000001', 'United State')

print(stock1)
print(type(stock1))
print((dir(stock1)))

def output_parameter(s):
    test_parameter(**s)

def test_parameter(**s):
    print(s)

output_parameter({'a':1, 'b':2})
test_parameter(a=1, b=2)