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
                raise Empty("Queue is empty")
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
                raise Empty("Queue is empty")
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