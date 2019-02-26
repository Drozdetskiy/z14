class BinomialCoefficients:
    def __init__(self, n):
        self.n = n+1
        self._prev_line = [0 for _ in range(n+1)]
        self._new_line = []
        self.index1 = 0
        self.index2 = 0

    def __next__(self):
        while self.index1 < self.n:
            _res = (self._prev_line[self.index2-1] +
                    self._prev_line[self.index2]) \
                if self.index2 else 1

            self._new_line.append(_res)
            self.index2 += 1

            if self.index2 == self.n:
                self._prev_line, self._new_line = self._new_line, []
                self.index2 = 0
                self.index1 += 1

            if (self.index1 >= self.n-1) and _res:
                return _res
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    a = BinomialCoefficients(5)
    for index2 in a:
        print(index2)
