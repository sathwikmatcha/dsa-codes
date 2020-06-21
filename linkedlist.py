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