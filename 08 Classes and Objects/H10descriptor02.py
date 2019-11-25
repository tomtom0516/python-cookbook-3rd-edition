# When I call area, in fact lazyproperty(area) is called, so lazy is called

def lazyproperty(func):
    print('I am lazyproperty({})'.format(func.__name__))
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @lazyproperty
    def area(self):
        print('Computed area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computed perimeter')
        return 2 * math.pi * self.radius


print(dir(Circle))