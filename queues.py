print("Welcome to queues")

class Queue:
    '''Class for Queue Implementations'''
    class ArrayQueue:
        '''Class for Python List Based Queue Implementation'''
       
        def __init__(self):
            self.def_cap = 10
            self._data=[None]*(self.def_cap)
            self._size=0
            self._front=0
            self._pos=0
        def is_empty(self):
            return (self._size==0)
        def len(self):
            return self._size
        def first(self):
            '''return the first element but donot remove that element from the queue'''
            if not(self.is_empty()):
                return self._data[self._front]
            else:
                raise TypeError("Queue is empty")
        def push(self,e):
            '''push element to the possible end of queue'''
            if(self.len()<self.def_cap):
                self._data[self._pos]=e
                self._pos=(self._pos+1)%len(self._data)
                self._size+=1
            else:
                self._resize()
                self.push(e)
        def dequeue(self):
            '''pops out the first element of the queue'''
            if not(self.is_empty()):
                self._data[self._front]=None
                self._front+=1
                self._size-=1
                if(self.is_empty()):
                    self._front=0
                    self._pos=0
            else:
                raise TypeError("Queue is empty")
        def _resize(self):
            self._pos=self.def_cap
            self.def_cap*=2
            temp=[None]*(self.def_cap)
            for i in range(len(temp)):
                temp[i]=self._data[self._front]
                self._front=(self._front+1)%len(self._data)
            self._data=temp
            self._front=0
        def print_queue(self):
            print(self._data)

    class linkedQueue:
        '''Queue Implementation through linked lists'''
        class _Node:
            def __init__(self, element, after):
                self._element = element
                self._after = after

        def __init__(self):
            self._head = None
            self._tail = None
            self._size = 0
        '''len,is_empty methods'''

        def is_empty(self):
            return self._size == 0

        def __len__(self):
            return self._size

        def push(self, e):
            '''pushes e into queue'''
            node = self._Node(e, None)
            if(self.is_empty()):
                self._head = node
                self._tail = node
            else:
                self._tail._after = node
            self._tail = node
            self._size += 1

        def top(self):
            '''returns first element without removal'''
            if not(self.is_empty()):
                return self._head._element
            else:
                raise TypeError("Empty Queue")

        def pop(self):
            '''returns and removes first element of queue'''
            if (self.is_empty()):
                raise TypeError("Empty Queue")
            else:
                temp = self._head
                ans = temp._element
                self._head = self._head._after
                self._size -= 1
                if(self.is_empty()):
                    self._tail = None
                temp = None
                return ans

'''Check comments for Array Queue Implementation'''
'''
q=Queue.ArrayQueue()
print(q.is_empty())
for i in range(5):
    q.push(i)
q.print_queue()
q.dequeue()
q.dequeue()
for i in range(6):
    q.push(10+i)
q.print_queue()
print(q.len())
for i in range(20):
    q.push(100+i)
print(q.len())
q.print_queue()
'''
'''check comments for linked list queue implementation'''
'''
llq=linkedList.linkedQueue()
for i in range(5):
    llq.push(i)
print(llq.top())
print(len(llq))
llq.push(10)
print(llq.top())
print(len(llq))
print(llq.pop())
print(llq.pop())
print(llq.pop())
print(len(llq))
'''
