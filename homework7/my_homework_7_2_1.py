from random import randint
from my_homework7_2_2 import DataNode


class Queue:
    def __init__(self, max_length=-1):
        self.head = None
        self.tail = None
        self._counter = 0
        self.max_length = max_length

    def enqueue(self, data):
        if self.max_length == -1 or self.max_length > self._counter:
            if self._counter:
                _temp = self.tail
                self.tail = DataNode(data, None)
                _temp.next_element = self.tail
            else:
                self.head = DataNode(data, None)
                self.tail = self.head

            self._counter += 1

        else:
            print('Queue is full')

    def dequeue(self):
        if self._counter:
            _result = self.head.data
            self.head = self.head.next_element
            self._counter -= 1
            return _result
        else:
            print('Queue is empty')

    def peek(self):
        return self.head.data if self._counter else print('Queue is empty')

    def count(self):
        return self._counter

    def get_queue(self):
        _temp = self.head
        _list = []
        while _temp:
            _list.append(_temp.data)
            _temp = _temp.next_element
        return _list


if __name__ == '__main__':
    q = Queue(3)
    for _ in range(5):
        q.enqueue(randint(-100, 100))
    print(q.get_queue(), q.count())

    print('#'*50)

    q = Queue()
    for _ in range(randint(5, 20)):
        q.enqueue(randint(-100, 100))
    print(q.get_queue(), q.count())

    print('#' * 50)

    while q.count():
        print(q.dequeue())

    print(q.dequeue())

    print('#' * 50)

    for _ in range(randint(5, 20)):
        q.enqueue(randint(-100, 100))
    print(q.get_queue())
    print(q.peek())

    for _ in range(q.count()-3):
        q.dequeue()

    print(q.get_queue())

    print('#' * 50)

    for _ in range(randint(5, 20)):
        q.enqueue(randint(-100, 100))
    print(q.get_queue(), q.count())
    print(q.peek())
    q.head.data = 9
    _tmp = q.head.next_element
    _tmp.data = 17

    print(q.get_queue())

    print(q.peek())
