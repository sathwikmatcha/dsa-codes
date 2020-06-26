from positionalList import PositionalList


class prQ_Base:
    class _Item:
        def __init__(self, key, value):
            self._k = key
            self._v = value

        def __lt__(self, other):
            return self._k < other._k

    def is_empty(self):
        return len(self) == 0


class PriorityQueue(prQ_Base):
    def find_min(self):
        if(self.is_empty()):
            raise ValueError("Queue is Empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if(walk.element() < small.element()):
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return (self._data)

    def add(self, k, v):
        self._data.add_last(self._Item(k, v))

    def min(self):
        a = self.find_min()
        ans = a.element()
        return(ans._k, ans._v)

    def rem_min(self):
        p = self._find_min()
        ans = self._data.delete(p)
        return (ans._k, ans._v)