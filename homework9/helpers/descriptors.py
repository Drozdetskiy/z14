import math


class FigureDescriptor:
    def __init__(self, args, mod):
        self._args = args
        self._mod = mod

    def __get__(self, instance, owner):
        self._log = getattr(instance, '_descriptor_log', {})

        previous_result_cond = True \
            if hasattr(instance, f'_descriptor_{self._mod}') \
            else False

        for key in self._args:
            if getattr(instance, key) != self._log.get(key):
                previous_result_cond = False
                self._log[key] = getattr(instance, key)
        setattr(instance, '_descriptor_log', self._log)

        if previous_result_cond:
            return getattr(instance, f'_descriptor_{self._mod}')
        else:
            _result = getattr(self, self._mod, self.wrong_implementation)()
            setattr(instance, f'_descriptor_{self._mod}', _result)
            return _result

    def wrong_implementation(self):
        raise WrongImplementationError


class CircleFigureDescriptor(FigureDescriptor):
    def square(self):
        return math.pi * self._log['r'] ** 2

    def perimeter(self):
        return 2 * math.pi * self._log['r']


class RectangleFigureDescriptor(FigureDescriptor):
    def square(self):
        return self._log['a'] * self._log['b']

    def perimeter(self):
        return (self._log['a'] + self._log['b']) * 2


class TriangleFigureDescriptor(FigureDescriptor):
    def square(self):
        p = self.perimeter() / 2
        return (p * (p - self._log['a']) *
                (p - self._log['b']) *
                (p - self._log['c'])) ** 0.5

    def perimeter(self):
        return self._log['a'] + self._log['b'] + self._log['c']


class WrongImplementationError(Exception):
    pass


class PositiveNumberDescriptor:
    def __init__(self, _arg):
        self._result = None
        self._arg = _arg

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, f'_result_{self._arg}', value)
        else:
            raise WrongValue

    def __get__(self, instance, owner):
        return getattr(instance, f'_result_{self._arg}')


class WrongValue(Exception):
    pass
