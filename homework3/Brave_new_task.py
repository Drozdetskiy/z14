class Number:

    def __init__(self, number):
        self.number = number

    def __gt__(self, other):
        return True if f'{self.number}{other.number}' > \
                       f'{other.number}{self.number}' else False


def max_number(_list):
        return int(
            ''.join(map(str, sorted(_list, key=Number, reverse=True)))
        )\
            if _list else None


if __name__ == '__main__':
    assert max_number([234, 123, 98]) == 98234123
    assert max_number([1, 2, 3, 4]) == 4321
    assert max_number([]) is None
    assert max_number([98, 9, 34]) == 99834
    print('max_number - OK')
    print(max_number([234, 123, 98, 4325, 547, 876, 9, 234, 678, 9, 0]))
    print(max_number([234, ]))
