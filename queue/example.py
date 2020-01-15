#!/usr/bin/env python
# coding: utf-8


from abc import ABC, abstractmethod


class CustomQueue(ABC):
    def __init__(self):
        self.data = []

    @abstractmethod
    def enqueue(self):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    def qsize(self):
        return len(self.data)

    @property
    def queue(self):
        return self.data


class FIFOQueue(CustomQueue):
    """list를 이용하여 일반적인 FIFO 정책의 Queue 구현"""

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        result = self.data.pop(0) if len(self.data) > 0 else None
        return result


class LIFOQueue(CustomQueue):
    """list를 이용하여 LIFO 정책의 queue 구현"""

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        result = self.data.pop(-1) if len(self.data) > 0 else None
        return result


if __name__ == '__main__':
    fifo = FIFOQueue()

    fifo.enqueue('first_item')
    fifo.enqueue('second_item')

    print('Queue items: {}, size: {}'.format(fifo.queue, fifo.qsize()))

    first_dequeue = fifo.dequeue()
    second_dequeue = fifo.dequeue()
    third_dequeue = fifo.dequeue()

    print(
        'first dequeue: {}, second dequeue: {}, third dequeue: {}'.format(first_dequeue, second_dequeue, third_dequeue))
    print('final Queue items: {}, size: {}'.format(fifo.queue, fifo.qsize()))

    lifo = LIFOQueue()
    lifo.enqueue((1, 'first_item'))
    lifo.enqueue((3, 'third_item'))

    print('Queue items: {}, size: {}'.format(lifo.queue, lifo.qsize()))

    first_dequeue = lifo.dequeue()
    second_dequeue = lifo.dequeue()
    third_dequeue = lifo.dequeue()

    print(
        'first dequeue: {}, second dequeue: {}, third dequeue: {}'.format(first_dequeue, second_dequeue, third_dequeue)
    )
    print('final Queue items: {}, size: {}'.format(lifo.queue, lifo.qsize()))
