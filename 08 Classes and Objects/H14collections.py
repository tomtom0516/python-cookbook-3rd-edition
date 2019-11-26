# apart from List, Map, Set, Dictionary

import abc
import collections

for item in dir(collections):
    itemType = getattr(collections, item)
    print(item, itemType, type(itemType))

print(type(collections.Mapping))