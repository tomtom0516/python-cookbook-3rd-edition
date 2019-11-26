# Use for deserializing JSON
# For example, receive data = { 'year': 2012, 'month': 8, 'day': 29 }
# Use this technology can change it into object

import time

class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


    def __str__(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)


def test():
    x = MyDate(2019, 11, 23)
    y = MyDate.today()

    z = MyDate.__new__(MyDate)
    data = {'year':2012, 'month':8, 'day':29}
    for key, value in data.items():
        setattr(z, key, value)

    print(x, y, z)


if __name__ == "__main__":
    test()