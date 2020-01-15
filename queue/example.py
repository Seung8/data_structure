#!/usr/bin/env python
# coding: utf-8

# In[159]:


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
            


# In[150]:


fq = FIFOQueue()

fq.enqueue('first_item')
fq.enqueue('second_item')

print('Queue items: {}, size: {}'.format(fq.queue, fq.qsize()))

first_dequeue = fq.dequeue()
second_dequeue = fq.dequeue()
third_dequeue = fq.dequeue()

print('first dequeue: {}, second dequeue: {}, third dequeue: {}'.format(first_dequeue, second_dequeue, third_dequeue))
print('final Queue items: {}, size: {}'.format(fq.queue, fq.qsize()))


# In[162]:


fq = LIFOQueue()
fq.enqueue((1, 'first_item'))
fq.enqueue((3, 'third_item'))

print('Queue items: {}, size: {}'.format(fq.queue, fq.qsize()))

first_dequeue = fq.dequeue()
second_dequeue = fq.dequeue()
third_dequeue = fq.dequeue()

print('first dequeue: {}, second dequeue: {}, third dequeue: {}'.format(first_dequeue, second_dequeue, third_dequeue))
print('final Queue items: {}, size: {}'.format(fq.queue, fq.qsize()))


# In[ ]:




