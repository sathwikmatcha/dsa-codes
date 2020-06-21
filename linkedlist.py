class linkedList:
    '''Class for linked List implementations'''
    class linkedStack:
        '''stack implementation using linked lists'''
        class _Node:
            def __init__(self,element,after):
                self._element=element
                self._next=after
        def __init__(self):
            '''Remember that head is a NODE !!!'''
            self._head=None
            self._size=0
        def is_empty(self):
            return self._size==0
        def __len__(self):
            return self._size
        def push(self,e):
            '''adds element e to stack'''
            node=self._Node(e,self._head)
            self._head=node
            self._size+=1
        def top(self):
            '''returns top element without removing it'''
            if not(self.is_empty()):
                return self._head._element
            else:
                raise TypeError("Stack is empty")
        def pop(self):
            '''pops top element and removes it'''
            if(self.is_empty()):
                raise TypeError("Stack is empty")
            else:
                temp=self._head
                ans=temp._element
                self._head=temp._next
                temp=None
                self._size-=1
                return ans

    class linkedQueue:
        '''Queue Implementation through linked lists'''
        class _Node:
            def __init__(self, element,after):
                self._element = element
                self._after = after
        def __init__(self):
            self._head=None
            self._tail=None
            self._size=0
        '''len,is_empty methods'''
        def is_empty(self):
            return self._size==0
        def __len__(self):
            return self._size
        
        def push(self,e):
            '''pushes e into queue'''
            node = self._Node(e, None)
            if(self.is_empty()):
                self._head=node
                self._tail=node
            else:
                self._tail._after=node
            self._tail=node
            self._size+=1
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
                temp=self._head
                ans=temp._element
                self._head=self._head._after
                self._size-=1
                if(self.is_empty()):
                    self._tail=None
                temp=None
                return ans
        
'''
ll=linkedList.linkedStack()
for i in range(5):
    ll.push(i)
print(ll.pop())
print(ll.pop())
print(len(ll)) 
ll.push(10)
print(ll.top())
print(len(ll))           
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