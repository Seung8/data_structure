#!/usr/bin/env python
# coding: utf-8


class CustomStack:
    """list를 활용하여 간단한 스택 구현"""

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        result = self.data.pop(-1) if len(self.data) > 0 else None
        return result

    def items(self):
        return self.data


if __name__ == '__main__':
    stack = CustomStack()

    stack.push('first item')
    stack.push('second item')

    print('items: {}'.format(stack.items()))

    first_pop = stack.pop()
    second_pop = stack.pop()

    print('first pop: {}, second pop: {}'.format(first_pop, second_pop))
