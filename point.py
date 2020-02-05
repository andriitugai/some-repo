class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True

        return False

    def __repr__(self):
        return "Point (x={}, y={}, z={})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, coeff):
        return Point(self.x * coeff, self.y * coeff, self.z * coeff)

    def __rmul__(self, coeff):
        return Point(self.x * coeff, self.y * coeff, self.z * coeff)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


if __name__ == "__main__":
    p1 = Point(1, 2, 3)
    p2 = Point(5, 6, 7)
    print(p1)
    print(p1 + p2)
    print(p1 - p2)
    print(p2 * 30)

    a, b, c = 30*p2
    print(a, b, c)

