#!/usr/bin/env python
# coding: utf-8

# In[17]:


import queue

# 일반적인 FIFO 정책의 Queue 생성
fifo = queue.Queue()

# 데이터 삽입하기(Enqueue)
fifo.put('first_enqueue')
fifo.put('second_enqueue')

# 데이터 삽입 확인
print('Queue items: {}, size: {}'.format(list(fifo.queue), fifo.qsize()))

# 데이터 꺼내기(Dequeue)
fifo_first_dequeue = fifo.get()
fifo_second_dequeue = fifo.get()

# 꺼낸 데이터 확인
print('first dequeue: {}, second dequeue: {}, final queue size: {}'.format(
    fifo_first_dequeue, fifo_second_dequeue, fifo.qsize()
))


# In[ ]:




