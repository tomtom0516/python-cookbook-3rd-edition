# way 1
s = '{name} has {n} messages.'
s.format(name='Yapeng', n=44)

# way 2
name = 'Yapeng'
n = 44
s.format_map(vars())

# way 3
'%(name) has %(n) messages.' % vars()

# way 4
import string
s = string.Template('$name has $n messages.')
s.substitute(vars())

# Advanced 01
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Yapeng', 44)
s.format_map(vars(a))

# Advanced 02
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
s.format_map(safesub(vars()))

# Advanced 03
import sys
def substitute(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

print(substitute('Hello {name}'))
print(substitute('Your favorite color is {color}'))