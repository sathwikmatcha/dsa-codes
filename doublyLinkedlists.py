class _ddList:
    class _Node:
        def __init__(self,element,before,after):
            self._element=element
            self._before=before
            self._after=after
    def __init__(self):
        
        self._header=self._Node(None,None,None)
        self._tailer = self._Node(None, None, None)
        
        self._header._after=self._tailer
        self._tailer._before=self._header
        
        self._size=0
    
    def __len__(self):
        
        return self._size
    
    def is_empty(self):
        
        return self._size==0
    
    def _insert_between(self,e,pre,suc):
        node=self._Node(e,pre,suc)
        pre._after=node
        suc._before=node
        self._size+=1

        return node

    def _delete_between(self,node):
        B=node._before
        A=node._after

        B._after=A
        A._before=B
        
        ans=node._element

        node._before=node._after=node._element=None
        
        self._size-=1

        return ans