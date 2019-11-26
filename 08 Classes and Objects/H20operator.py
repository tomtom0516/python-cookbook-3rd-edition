import math
import operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
        
    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


def test():
    p = Point(3, 4)
    print(p.distance(0, 0))
    d = operator.methodcaller('distance', 0, 0)
    print(d(p))

    points = [
        Point(1, 2),
        Point(3, 0),
        Point(10, -3),
        Point(-5, -7),
        Point(-1, 8),
        Point(3, 2)
    ]

    # Sort by distance from origin (0, 0)
    points.sort(key=operator.methodcaller('distance', 0, 0))
    print(points)

if __name__ == "__main__":
    test()
