class _ddList:
    '''class created to make a doubly linked list and used for inheritance to other classes as a parent class '''
    class _Node:
        '''sub class to create a node'''
        def __init__(self,element,before,after):
            self._element=element
            self._before=before
            self._after=after
    def __init__(self):
        '''header and tailers are sentinels to escape exceptional cases of removal or addition'''
        self._header=self._Node(None,None,None)
        self._tailer = self._Node(None, None, None)
        '''initialisation of header and tailer'''
        self._header._after=self._tailer
        self._tailer._before=self._header
        
        self._size=0
    
    def __len__(self):
        '''returns length of ddlist'''
        return self._size
    
    def is_empty(self):
        '''checks whether ddlist is empty or not'''
        return self._size==0
    
    def _insert_between(self,e,pre,suc):
        '''inserts node between nodes pre,suc'''
        node=self._Node(e,pre,suc)
        pre._after=node
        suc._before=node
        self._size+=1

        return node

    def _delete_between(self,node):
        '''deletes node node from the ddlist'''
        B=node._before
        A=node._after

        B._after=A
        A._before=B
        
        ans=node._element

        node._before=node._after=node._element=None
        
        self._size-=1

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

    def add_left(self, e):
        '''Adds an element to the front of the deque'''
        self._insert_between(e, self._header, self._header._after)

    def add_right(self, e):
        '''adds an element to the back of the deque'''
        self._insert_between(e, self._tailer._before, self._tailer)

    def remove_left(self):
        '''removes element from the front'''
        self._delete_between(self._header._after)

    def remove_right(self):
        '''removes element from the back'''
        self._delete_between(self._tailer._before)


'''...............................................................................'''


