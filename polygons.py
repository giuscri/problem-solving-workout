import math
import unittest

def build_regular_polygon_class(nsides):
    class C:
        def __init__(self, side_len):
            self._side_len = side_len
        def calculate_perimeter(self):
            return self._side_len * nsides
        def calculate_area(self):
            return (self._side_len**2 * nsides) / \
                      (4 * math.tan(math.radians(180/nsides)))
    return C

regular_polygons = (
    ('Triangle', 3),
    ('Square', 4),
    ('Pentagon', 5),
    ('Hexagon', 6)
)

for name,nsides in regular_polygons:
    exec('{} = build_regular_polygon_class({})'.format(name, nsides))

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def calculate_permiter(self):
        return 2 * (self._width+self._height)
    def calculate_area(self):
        return self._height * self._width

class Circle:
    def __init__(self, radius): 
        self._radius = radius
    def calculate_perimeter(self):
        return 2 * math.pi**2 * self._radius
    def calculate_area(self):
        return math.pi * self._radius**2

class MainTest(unittest.TestCase):
    def test_circle(self):
        radius = 42
        c = Circle(radius)
        self.assertAlmostEqual(c.calculate_perimeter(), \
                                  2 * math.pi**2 * radius)

if __name__ == '__main__':
    unittest.main()
