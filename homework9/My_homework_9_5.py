class Fuctorial:
    def __init__(self, _n):
        self._n = _n
        self._index = 0
        self._res = 1

    def __next__(self):
        while self._index < self._n:
            self._index += 1
            self._res *= self._index
            return self._res
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    a = Fuctorial(5)
    for i in a:
        print(i)
