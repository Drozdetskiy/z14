class Fibonacci:
    def __init__(self, _n):
        self._n = _n
        self._f1 = 0
        self._f2 = 0
        self._index = 1

    def __next__(self):
        while self._index <= self._n:
            _res = self._f1 + self._f2 if self._f1 and self._f2 else 1
            self._f1, self._f2 = self._f2, _res
            self._index += 1
            return _res
        raise StopIteration


if __name__ == '__main__':
    fibonacci = Fibonacci(7)
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    print(next(fibonacci))
    try:
        print(next(fibonacci))
    except StopIteration:
        print('Stop iter')
