# Computed Properties
# replace the func.__name__ in __dict__ with computed value

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            print(self, instance, cls, self.func.__name__)
            value = self.func(instance)  # why instance here ???
            setattr(instance, self.func.__name__, value)
            return value

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

