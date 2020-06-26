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
        print("small= ", small)
        walk = self._data.after(small)
        print("walk= ", walk)
        i = 0
        while walk is not None:
            if(walk.element() < small.element()):
                small = walk
            walk = self._data.after(walk)
            print(i)
            i += 1
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        self._data.add_first(self._Item(k, v))

    def min(self):
        a = self.find_min()
        print(a)
        ans = a.element()
        return(ans._k, ans._v)

    def rem_min(self):
        p = self._find_min()
        ans = self._data.delete(p)
        return (ans._k, ans._v)


'''
p = PriorityQueue()
p.add(10, "A")
p.add(4, "E")
p.add(9, "W")
p.add(5, "Q")

print(p.min())
'''
