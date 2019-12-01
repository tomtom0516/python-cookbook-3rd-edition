x = 'Hello World'
print('o' in x)

import re
# no group & group match
re_no_group = re.compile(r'\d+/\d+/\d+')
re_group = re.compile(r'(\d+)/(\d+)/(\d+)')

input_ = '11/28/2019'
m1 = re_no_group.match(input_)
m1.group(0)
# m1.group(1)
m2 = re_group.match(input_)
m2.group(0)
m2.group(1)

# no group & group findall
y = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
re_no_group.findall(y)
re_group.findall(y)