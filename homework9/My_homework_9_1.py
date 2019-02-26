class MultiFileOpen:
    def __init__(self, *args):
        self.args = args

    def __enter__(self):
        self._files_list = list(map(lambda x: open(*x), self.args))
        return self._files_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        for _file in self._files_list:
            _file.close()
        print('files closed')
        print(exc_type, exc_val, exc_tb)


if __name__ == '__main__':
    with MultiFileOpen(('file1.txt', 'a'), ('file2.txt', 'a')) as files:
        for file in files:
            file.write('\n!!!')

    with MultiFileOpen(('file1.txt', 'r'), ('file2.txt', 'rb')) as files:
        for file in files:
            print(file.read())
