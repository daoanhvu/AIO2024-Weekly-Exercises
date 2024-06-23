

class MyStack():
    def __init__(self, capacity) -> None:
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        l = len(self.__stack)
        if l < self.__capacity:
            self.__stack.insert(0, value)

    def top(self):
        if len(self.__stack) > 0:
            return self.__stack[0]
        else:
            return None


class MyQueue:
    def __init__(self, capacity) -> None:
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        l = len(self.__queue)
        if l < self.__capacity:
            self.__queue.insert(0, value)

    def dequeue(self):
        pass

    def front(self):
        if len(self.__queue) > 0:
            return self.__queue[-1]
        else:
            return None


if __name__ == '__main__':
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.is_full())

    stack1 = MyStack(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.top())

    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.is_full())

    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.front())
