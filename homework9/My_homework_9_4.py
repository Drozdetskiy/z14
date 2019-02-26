class EvenGenerator:
    def __init__(self, n):
        self.n = n
        self.index = -2

    def __next__(self):
        if self.index >= self.n-1:
            raise StopIteration
        self.index += 2
        return self.index

    def __iter__(self):
        return self


if __name__ == '__main__':
    evens = EvenGenerator(10)
    for i in evens:
        print(i)
