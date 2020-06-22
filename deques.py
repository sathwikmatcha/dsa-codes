from collections import deque

class deques_collection:
    def __init__(self):
        self.D=deque()
    def len(self):
        return len(self.D)
    def add_first(self,e):
        self.D.appendleft(e)
    def add_last(self,e):
        self.D.append(e)
    def delete_first(self):
        self.D.popleft()
    def delete_last(self):
        self.D.pop()
    def first(self):
        return self.D[0]
    def last(self):
        self.D[-1]


class _ddList:
    class _Node:
        def __init__(self, element, before, after):
            self._element = element
            self._before = before
            self._after = after

    def __init__(self):

        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)

        self._header._after = self._tailer
        self._tailer._before = self._header

        self._size = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def _insert_between(self, e, pre, suc):
        node = self._Node(e, pre, suc)
        pre._after = node
        suc._before = node
        self._size += 1

        return node

    def _delete_between(self, node):
        B = node._before
        A = node._after

        B._after = A
        A._before = B

        ans = node._element

        node._before = node._after = node._element = None

        self._size -= 1

        return ans



class LinkedDeque(_ddList):
    
    def first(self):
        '''returns the front element of deque'''
        if(self.is_empty()):
            raise TypeError("Deque is empty")
        else:
            return self._header._after._element
    
    def last(self):
        '''returns the last element of deque'''
        if(self.is_empty()):
            raise TypeError("Deque is empty")
        else:
            return self._tailer._before._element
    def add_left(self,e):
        '''Adds an element to the front of the deque'''
        self._insert_between(e,self._header,self._header._after)
    def add_right(self,e):
        '''adds an element to the back of the deque'''
        self._insert_between(e,self._tailer._before,self._tailer)
    def remove_left(self):
        '''removes element from the front'''
        self._delete_between(self._header._after)
    def remove_right(self):
        '''removes element from the back'''
        self._delete_between(self._tailer._before)
    

'''...............................................................................'''





'''check comments for deques_collection'''
'''
d=deques_collection()
print(d.len())
'''
'''check comments for linkedDeque'''
dd=LinkedDeque()
dd.add_left(1)
dd.add_right(2)
print(len(dd))
print(dd.first())
dd.remove_left()
dd.add_left(3)
print(dd.first())

