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
                raise Empty("Stack is empty")
        def rem_top(self):
            if not (self.is_empty()):
                a=self._data.pop()
                return a 
            else:
                raise Empty("Staxk is empty")
    

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