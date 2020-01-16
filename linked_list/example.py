#!/usr/bin/env python
# coding: utf-8


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    self.add(): 맨 뒤에 아이템 추가
    self.desc(): 모든 노드 아이템 출력
    """
    def __init__(self, data):
        # 최초 첫 번째 노드 생성
        self.head = Node(data)

    def add(self, data):
        node = self.head

        # node.next 가 None 이면 다음 노드로 이동(마지막 노드 탐색)
        while node.next:
            node = node.next

        # 새 노드 생성
        node.next = Node(data)

    def desc(self):
        node = self.head

        # 모든 node 순회하며 출력
        while node:
            print(node.data)
            # node 출력 후 node 변수에 다음 노드 지정
            node = node.next


if __name__ == '__main__':
    pass
