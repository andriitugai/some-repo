import math

class Circle(object):
    def __init__(self, radius = 1):
        self._radius = radius

    @property
    def radius(self):
        return self._radius 

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError('Radius cannot be negative')

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, diameter):
        setattr(self, 'radius', diameter / 2)

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f'{self.__class__}({self._radius})'

    def __str__(self):
        return f'{self.__class__.__name__}({self._radius})'


# 649087-20191201-cdeca7a6
    



def main():
    c1 = Circle(5)
    print(f'Circle 1: Radius = {c1.radius}, Diameter = {c1.diameter}, Area = {c1.area}')

    c0 = Circle()
    print(f'Circle 0: Radius = {c0.radius}, Diameter = {c0.diameter}, Area = {c0.area}')

    print(c0, c1)

    print("Modifying!")

    c0.radius = 5
    print(f'Circle 0: Radius = {c0.radius}, Diameter = {c0.diameter}, Area = {c0.area}')

    c1.diameter = 8
    print(f'Circle 1: Radius = {c1.radius}, Diameter = {c1.diameter}, Area = {c1.area}')

    c1.diameter = -4

    # c1.radius = -5

if __name__ == '__main__':
    main()
