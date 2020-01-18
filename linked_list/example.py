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
    self.delete(): 특정 노드 삭제
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
            print('data: {}'.format(node.data))
            # node 출력 후 node 변수에 다음 노드 지정
            node = node.next

    def delete(self, data):
        if not self.head:
            print('제거할 데이터 없음')
            return

        # 맨 앞 노드(self.head)를 삭제하는 경우
        if self.head.data == data:
            temp = self.head
            self.head = temp.next
            del temp

        # 중간 노드 혹은 마지막 노드를 삭제하는 경우
        else:
            node = self.head
            # 마지막 노드까지 순회
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = temp.next
                    del temp
                    return
                else:
                    node = node.next

    def search(self, data):
        """특정 데이터 순차 탐색"""
        node = self.head

        while node:
            if node.data == data:
                print('검색 결과: ', node.data)
                break
            node = node.next


# 테스트
if __name__ == '__main__':
    print('## 연결 리스트 생성')
    linked_list1 = LinkedList(0)
    linked_list1.desc()

    print('## 헤드 제거')
    linked_list1.delete(0)
    linked_list1.desc()

    print('## 0부터 9까지 노드 생성 후 출력')
    linked_list2 = LinkedList(0)

    for i in range(1, 10):
        linked_list2.add(i)
    linked_list2.desc()

    print('## 중간 노드 4 삭제 후 출력')
    linked_list2.delete(4)
    linked_list2.desc()

    print('## 데이터가 9인 노드 검색')
    linked_list2.search(9)
