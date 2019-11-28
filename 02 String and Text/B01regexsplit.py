import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

re.split(r'[\s,;]\s*', line)

# Discussion
# capture group
x = [ s for s in range(10)]
print(x)


