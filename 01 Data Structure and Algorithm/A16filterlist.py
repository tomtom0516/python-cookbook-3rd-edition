rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# generator
rows_filtered = (item for item in rows if item['date'] == '07/02/2012')
for item in rows_filtered:
    print(item)

# filter
rows_filtered = filter(lambda s: s['date'] == '07/02/2012', rows)
for item in rows_filtered:
    print(item)

# compress
from itertools import compress
filter_compress = [n['date'] == '07/02/2012' for n in rows]
print(filter_compress)
print(list(compress(rows, filter_compress)))