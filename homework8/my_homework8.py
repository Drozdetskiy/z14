from math import pi


class InvalidGeometry(Exception):
    pass


class WrongValueError(Exception):
    pass


class Figure:
    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __str__(self):
        return f'{self.__class__.__name__}:"{self.name}"'

    def square(self):
        pass

    def perimeter(self):
        pass


class Triangle(Figure):
    def __init__(self, name, a, b, c):
        if a + b <= c or b + c <= a or a + c <= b:
            raise InvalidGeometry

        if (a or b or c) <= 0:
            raise WrongValueError

        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        _half_perimeter = self.perimeter()/2
        return (_half_perimeter *
                (_half_perimeter - self.a) *
                (_half_perimeter - self.b) *
                (_half_perimeter - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


class Circle(Figure):
    def __init__(self, name, r):
        if r <= 0:
            raise WrongValueError

        super().__init__(name)
        self.r = r

    def square(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2*pi*self.r


class Rectangle(Figure):
    def __init__(self, name, a, b):
        if (a or b) <= 0:
            raise WrongValueError

        super().__init__(name)
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2


if __name__ == '__main__':
    try:
        circles = [Circle(name=f'r={i}', r=i) for i in range(1, 5)]
    except WrongValueError:
        print('WrongValueError in circles')
        circles = []
    try:
        rectangles = [Rectangle(name=f'a={i}, b={i ** 2}', a=i, b=i ** 2)
                      for i in range(1, 5)]
    except WrongValueError:
        print('WrongValueError in rectangles')
        rectangles = []
    try:
        triangles = [
            Triangle(
                name=f'a={i + 1},'f' b={i ** 2},'f' c={(i + i ** 2) // 2}',
                a=i + 1,
                b=i ** 2,
                c=(i + i ** 2) // 2)
            for i in range(1, 4)
        ]
    except InvalidGeometry:
        print('Triangle geometry is wrong')
        triangles = []
    except WrongValueError:
        print('WrongValueError in triangles')
        triangles = []

    figures = circles + triangles + rectangles
    for figure in figures:
        print(f'My name is: {figure}')
        assert str(figure) == f'{figure.__class__.__name__}:"{figure.name}"'
        print(f'My perimeter is: {figure.perimeter()}')
        print(f'My square is: {figure.square()}', end=f"\n{'-' * 35}\n")

    try:
        assert Circle(name='1', r=2) == Circle(name='2', r=2)
        assert Circle(name='1', r=2) < Circle(name='2', r=4)
        assert Circle(name='1', r=4) >= Circle(name='2', r=4)
    except WrongValueError:
        print('WrongValueError in circles')

    try:
        assert Rectangle(name='1', a=2, b=3) == Rectangle(name='2', b=2, a=3)
        assert Rectangle(name='1', a=2, b=3) < Rectangle(name='2', a=4, b=10)
        assert Rectangle(name='1', a=4, b=2) >= Rectangle(name='2', a=4, b=1)
    except WrongValueError:
        print('WrongValueError in rectangles')

    try:
        assert Triangle(name='1', a=2, b=3, c=4) == Triangle(name='2', b=2, a=3, c=4)
        assert Triangle(name='1', a=2, b=3, c=1.5) < Triangle(name='2', a=4, b=10, c=7)
        assert Triangle(name='1', a=4, b=2, c=5) >= Triangle(name='2', a=4, b=5, c=1)
    except InvalidGeometry:
        print('Triangle geometry is wrong')
        triangles = []
    except WrongValueError:
        print('WrongValueError in triangles')
    finally:
        print('ok')
