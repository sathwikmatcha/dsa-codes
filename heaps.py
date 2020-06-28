from priorityqueue import prQ_Base


class heapPriorityQueueArray(prQ_Base):
    # non-public
    def _parent(self, p):
        return (p-1)//2

    def _left(self, p):
        return 2*p+1

    def _right(self, p):
        return 2*p+2

    def _has_left(self, p):
        return (2*p+1 < len(self._data))

    def _has_right(self, p):
        return (2*p+2 < len(self._data))

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, i):
        parent = self._parent(i)
        par_element = self._data[parent]
        if(self._data[i] < par_element):
            self._swap(i, parent)
            self._upheap(parent)

    def _downheap(self, j):
        e = self._data[j]
        c = 0
        cnt = 0
        small_child = None
        if(self._has_left(j)):
            le = self._data[self._left(j)]
            c = 1
            cnt += 1
        if(self._has_right(j)):
            re = self._data[self._right(j)]
            c = 2
            cnt += 1
        if(c == 1 and cnt == 1):
            # only left child
            small_child = self._left(j)
            self._swap(j, small_child)
            self._downheap(small_child)
        if(c == 2 and cnt == 1):
            # only right
            small_child = self._right(j)
            self._swap(j, small_child)
            self._downheap(small_child)
        if(cnt == 2):
            # compare left and right
            if(le <= re):
                small_child = self._left(j)
                self._swap(j, small_child)
                if(self._data[small_child] < re):
                    self._swap(small_child, self._right(small_child))
                    self._downheap(small_child)

            else:
                small_child = self._right(j)
                self._swap(j, small_child)
                if(self._data[small_child] < le):
                    self._swap(small_child, self._left(small_child))
                    self._downheap(small_child)
    # public methods

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        e = self._Item(key, value)
        self._data.append(e)
        self._upheap(len(self._data)-1)

    def min(self):
        if(self.is_empty()):
            raise ValueError("Empty Heap")
        else:
            item = self._data[0]
            return (tem._k, item._v)

    def rem_min(self):
        if(self.is_empty()):
            raise ValueError("Empty Heap")
        else:
            a = self._data.pop()
            self._downheap(0)
            return (a._k, a._v)
