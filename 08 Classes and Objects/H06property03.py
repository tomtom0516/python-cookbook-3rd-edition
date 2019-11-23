# computed property
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return self.radius ** 2 * math.pi
    
    @property
    def diameter(self):
        return self.radius * 2 * math.pi

def test():
    c = Circle(5.0)
    print('raidus is {0.radius} area is {0.area}, diameter is {0.diameter}'.format(c))

if __name__ == "__main__":
    test()
