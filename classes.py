class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __str__(self):
        return f'Point ({self.x},{self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # defining class level methods
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'Point ({self.x}, {self.y})')


point1 = Point(22, 56)
point2 = Point(2, 5)
zeroPoint = Point.zero()
point1.draw()
zeroPoint.draw()
print(f'Point1 : {point1}')
print(f'point1 == point2 : {point1 == point2}')
print(f'point1 > point2 : {point1 > point2}')
print(f'point1 + point2 : {point1 + point2}')
print(f'point1 > point2 : {point1 > point2}')
print(f'Restrict to push in main branch')


