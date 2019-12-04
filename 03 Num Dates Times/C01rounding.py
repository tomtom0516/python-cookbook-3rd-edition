# way 1 round function
round(1.23, 1)
# 1.2
round(1.27, 1)
# 1.3
round(-1.27, 1)
# -1.3
round(1.25361,3)
# 1.254
a = 1627731
round(a, -1)
# 1627730
round(a, -2)
# 1627700
round(a, -3)
# 1628000

# way 2 format function
x = 1.23456
format(x, '0.2f')
# '1.23'
format(x, '0.3f')
#'1.235'
'value is {:0.3f}'.format(x)
# 'value is 1.235'

# float accuracy, could be solved by decimal module
a = 2.1
b = 4.2
c = a + b

# >>> a = 2.1
# >>> b = 4.2
# >>> c = a + b
# >>> c
# 6.300000000000001