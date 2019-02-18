from random import randint


class DataNode:
    def __init__(self, data, next_element):
        self.data = data
        self.next_element = next_element


class Stack:
    def __init__(self, max_length=-1):
        self.max_length = max_length
        self._counter = 0
        self.top = None

    def push(self, data):
        if self.max_length == -1 or self.max_length > self._counter:
            self.top = DataNode(data, self.top)
            self._counter += 1
        else:
            print('Stack overflow')

    def pop(self):
        if self._counter:
            _result = self.top.data
            self.top = self.top.next_element
            self._counter -= 1
            return _result
        else:
            print('Stack is empty')

    def peek(self):
        return self.top.data if self._counter else print('Stack is empty')

    def count(self):
        return self._counter

    def get_stack(self):
        _temp = self.top
        _list = []
        while _temp:
            _list.append(_temp.data)
            _temp = _temp.next_element
        return _list


if __name__ == '__main__':
    s = Stack(5)
    for _ in range(s.max_length):
        s.push(randint(-100, 100))
    while s.count():
        print(s.pop())

    print('#'*50)

    for i in range(s.max_length):
        s.push(randint(-100, 100))
    print(s.get_stack())

    print('#' * 50)

    s = Stack()
    for _ in range(randint(5, 20)):
        s.push(randint(-100, 100))
    print(s.get_stack())
