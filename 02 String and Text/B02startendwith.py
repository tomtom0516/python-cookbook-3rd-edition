x = ['foo.c', 'spam.c', 'spam.h']
y = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
[d for d in x if d.endswith(('.c', '.h'))]
[d.endswith(('.c', '.h')) for d in y]
