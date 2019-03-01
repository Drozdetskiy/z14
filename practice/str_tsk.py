import re


def sorted_by_innumbers(_str):
    _str_list = _str.split()
    return sorted(_str_list, key=lambda x: re.findall(r'\d+', x))


if __name__ == '__main__':
    print(sorted_by_innumbers("th2e asd1f s3df s4d f5, dsfds7, 6f, sd1"))
