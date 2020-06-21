print("Welcome to python stacks")
import time
class Stack:
    ''' Different Implementations of stacks'''
    
    class ArrayStack:
        '''Python List implementation of stack'''
        
        '''init function'''
        def __init__(self):
            self._data=[]
        '''empty check'''
        def is_empty(self):
            return (len(self._data)==0)
        '''length of stack'''
        def len(self):
            return len(self._data)
        '''push element e to stack'''
        def push(self,e):
            self._data.append(e)
        '''returns top element without removing it.brings error if stack is empty'''
        def top(self):
            if not (self.is_empty()):
                return self._data[-1]
            else:
                raise TypeError("Stack is empty")
        def rem_top(self):
            if not (self.is_empty()):
                a=self._data.pop()
                return a 
            else:
                raise TypeError("Staxk is empty")
    
    class linkedStack:
        '''stack implementation using linked lists'''
        class _Node:
            def __init__(self, element, after):
                self._element = element
                self._next = after

        def __init__(self):
            '''Remember that head is a NODE !!!'''
            self._head = None
            self._size = 0

        def is_empty(self):
            return self._size == 0

        def __len__(self):
            return self._size

        def push(self, e):
            '''adds element e to stack'''
            node = self._Node(e, self._head)
            self._head = node
            self._size += 1

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
                temp = self._head
                ans = temp._element
                self._head = temp._next
                temp = None
                self._size -= 1
                return ans

'''check comments for array implementation'''
'''
stack_inst=Stack.ArrayStack()
print(stack_inst.is_empty())
stack_inst.push(1)
stack_inst.push(2)
print(stack_inst.is_empty())
print(stack_inst.len())
print(stack_inst.rem_top())
print(stack_inst.top())
print(stack_inst.is_empty())
'''
'''check comments for linkedlist implementation'''
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
