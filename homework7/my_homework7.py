import sys

from helpers.converter import DataConverter


if __name__ == '__main__':
    paths = sys.argv[1:]
    data_container = DataConverter(*paths)
    data_container.convert()
