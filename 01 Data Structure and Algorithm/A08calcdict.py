prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print('prices.items(): \t', prices.items())
print('prices.keys():  \t', prices.keys())
print('prices.values():\t', prices.values())


# Sort
print(prices)
print(dict(sorted(prices.items())))
print(dict(sorted(prices.items(), key=lambda s: prices[s[0]], reverse=True)))
print(prices)


my_list = [{'a': 1}, {'b': 2}, {'c': 0}]
# my_list.sort(key=lambda s: list(s.values())[0])
print(my_list)
print(sorted(my_list, key=lambda s: list(s.values())[0]))
print(my_list)
