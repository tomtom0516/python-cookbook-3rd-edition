from urllib.request import urlopen

baidu = urlopen('https://www.baidu.com')

for line in baidu:
    print(line.decode('utf-8'), end='')

