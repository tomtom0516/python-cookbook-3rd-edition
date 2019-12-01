import re
num = re.compile('\d+')
# ASCII digits
num.match('123')
# Arabic digits
num.match('\u0661\u0662\u0663')

print('\u0661\u0662\u0663')

