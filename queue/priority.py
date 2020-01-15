#!/usr/bin/env python
# coding: utf-8

# In[32]:


import queue


# 우선순위대로 싱행하는 PriorityQueue 생성
priority = queue.PriorityQueue()

# 우선순위를 가진 데이터 삽입 PriorityQueue.put((우선순위, 데이터))
priority.put((3, 'third item'))
priority.put((1, 'first item'))
priority.put((2, 'second item'))

# 데이터 삽입 확인
print(
    'Queue items: {}, size: {}'.format(list(priority.queue), priority.qsize())
)

# 데이터 꺼내기
first_dequeue = priority.get()
second_dequeue = priority.get()
third_dequeue = priority.get()
print(
    'first dequeue: {}, second dequeue: {}, third dequeue: {}'.format(first_dequeue[1], second_dequeue[1], third_dequeue[1])
)

print('final Queue items: {}, size: {}'.format(list(priority.queue), priority.qsize()))


# In[ ]:




