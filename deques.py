from collections import deque

class deques:
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
d=deques()
print(d.len())