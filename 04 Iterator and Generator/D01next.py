# with open('somefile.txt') as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass


with open('somefile.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


items = [1, 2, 3]
it = iter(items)
