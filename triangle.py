import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        def side_length(point1, point2):
            return math.hypot((point2[0] - point1[0]), (point2[1] - point1[1]))

        self.ab = side_length(self.a, self.b)
        self.bc = side_length(self.b, self.c)
        self.ca = side_length(self.c, self.a)

    def existence(self):
        if (self.a == self.b or self.a == self.c or self.b == self.c) or \
                (self.ab >= self.bc + self.ca or self.bc >= self.ab + self.ca or self.ca >= self.ab + self.bc):
            return False
        else:
            return True

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))


if __name__ == '__main__':
    a_point = [int(x) for x in input("Enter the coordinates x,y of the A point: ").split(',')]
    b_point = [int(x) for x in input("Enter the coordinates x,y of the B point: ").split(',')]
    c_point = [int(x) for x in input("Enter the coordinates x,y of the C point: ").split(',')]

    triangle = Triangle(a_point, b_point, c_point)

    if triangle.existence():
        print('Triangle perimeter is', triangle.perimeter())
        print('Triangle area is', triangle.area())
    else:
        print("Triangle doesn't exist")
