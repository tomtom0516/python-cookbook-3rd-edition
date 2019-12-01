x = '我'
print(ascii(x))

y = '是'
print(ascii(y))

z = '我是一只来自北方的狼'
print(ascii(z))

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1, s2)
print(ascii(s1), ascii(s2))

print(s1.encode('utf-8'))
print(s2.encode('utf-8'))