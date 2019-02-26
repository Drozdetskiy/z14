from helpers.descriptors import \
    CircleFigureDescriptor, \
    RectangleFigureDescriptor, \
    TriangleFigureDescriptor, \
    PositiveNumberDescriptor
from functools import total_ordering


class MetaFigure(type):
    def __init__(cls, name, bases, nmspc):
        for arg in nmspc['args']:
            setattr(cls, arg, PositiveNumberDescriptor(f'_{arg}'))
        super(MetaFigure, cls).__init__(name, bases, nmspc)


@total_ordering
class Figure(metaclass=MetaFigure):
    args = ()

    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def square(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    def __le__(self, other):
        return self.square <= other.square

    def __str__(self):
        return f'{self.__class__.__name__}:"{self.name}"'


class FigureException(Exception):
    pass


class Triangle(Figure):
    args = ('a', 'b', 'c')

    square = TriangleFigureDescriptor(args, mod='square')
    perimeter = TriangleFigureDescriptor(args, mod='perimeter')


class Circle(Figure):
    args = ('r', )

    square = CircleFigureDescriptor(args, mod='square')
    perimeter = CircleFigureDescriptor(args, mod='perimeter')


class Rectangle(Figure):
    args = ('a', 'b')

    square = RectangleFigureDescriptor(args, mod='square')
    perimeter = RectangleFigureDescriptor(args, mod='perimeter')


if __name__ == '__main__':
    a = Circle(name='ar', r=12)
    b = Circle(name='br', r=15)
    print(a > b, a < b, a != b, a == b, a >= b, a <= b)
    print(a.r)

    circles = [Circle(name=f'r={i}', r=i) for i in range(1, 5)]
    rectangles = [
        Rectangle(name=f'a={i}, b={i**2}',
                  a=i, b=i**2) for i in range(1, 5)
    ]
    try:
        triangles = [
            Triangle(name=f'a={i+1}, b={i**2}, c={(i + i**2)//2}',
                     a=i+1, b=i**2, c=(i + i**2)//2) for i in range(1, 4)
        ]
    except FigureException as exp:
        triangles = []
        print(f'Triangle exception {exp}')

    figures = circles + rectangles + triangles

    for figure in figures:
        print(f'My name is: {figure}')
        assert str(figure) == f'{figure.__class__.__name__}:"{figure.name}"'
        print(f'My perimeter is: {figure.perimeter}')
        print(f'My square is: {figure.square}', end=f"\n{'-'*35}\n")

    assert Circle(name='1', r=2) == Circle(name='2', r=2)
    assert Circle(name='1', r=2) < Circle(name='2', r=4)
    assert Circle(name='1', r=4) >= Circle(name='2', r=4)

    assert Rectangle(name='1', a=2, b=3) == Rectangle(name='2', b=2, a=3)
    assert Rectangle(name='1', a=2, b=3) < Rectangle(name='2', a=4, b=10)
    assert Rectangle(name='1', a=4, b=2) >= Rectangle(name='2', a=4, b=1)

    try:
        assert Triangle(name='1', a=2, b=3, c=4) == Triangle(name='2', b=2, a=3, c=4)
        assert Triangle(name='1', a=2, b=3, c=1.5) < Triangle(name='2', a=4, b=10, c=7)
        assert Triangle(name='1', a=4, b=2, c=5) >= Triangle(name='2', a=4, b=5, c=1)
    except FigureException as exp:
        print(f'Triangle exception {exp}')
