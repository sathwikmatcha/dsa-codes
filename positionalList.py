from deques import _ddList as _ddList
'''..................................................................................'''


class PositionalList(_ddList):

    class _Position:

        def __init__(self, container, node):

            self._container = container
            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self, other):

            statement = False
            if(type(other) == type(self)):
                if(other._node == self._node):
                    statement = True
            return statement

        def __ne__(self, other):

            statement = True
            if(type(other) == type(self)):
                if(other._node == self._node):
                    statement = False
            return statement

    def _validate(self, p):

        if not(isinstance(p, self._Position)):
            raise TypeError("p is not position instance")

        if(p._container != self):
            raise TypeError("p does not belong to this list")

        if(p._node._after == None or p._node._before == None):
            raise ValueError("p is not valid")

        return p._node

    def _make_position(self, node):

        if(node is self._header or node is self._tailer):
            return None
        pos = self._Position(self, node)
        return pos

    def first(self):
        '''returns the first position of this positional list'''
        if(self.is_empty()):
            return None
        else:
            return self._Position(self, self._header._after)

    def last(self):
        '''returns the last position of this positional list'''
        if(self.is_empty()):
            return None
        else:
            return self._Position(self._tailer._before)

    def add_first(self, e):
        '''adds element e to front'''
        a = self._insert_between(e, self._header, self._header._after)
        pos = self._Position(self, a)
        return pos

    def add_last(self, e):
        '''adds element e to last'''
        a = self._insert_between(e, self._tailer, self._tailer._before)
        pos = self._Position(self, a)
        return pos

    def add_before(self, p, e):
        '''adds element e to postion before p and returns new position'''
        a = self._validate(p)
        new_node = self._insert_between(e, a._before, a)
        pos = self._Position(self, new_node)
        return pos

    def add_after(self, p, e):
        '''adds element e to position after p and returns new position'''
        a = self._validate(p)
        new_node = self._insert_between(e, a, a._after)
        pos = self._Position(self, new_node)
        return pos

    def replace(self, p, e):
        '''replaces element at p with e and returns new position'''
        a = self._validate(p)
        a._element = e
        pos = self._Position(self, a)
        return pos

    def delete(self, p):
        '''delete the node at position p and returns deleted element'''
        a = self._validate(p)
        old_val = a._element
        self._delete_between(a)
        return old_val

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._after)

    def __iter__(self):
        '''gives a forward iteration of elements'''
        a = self.first()
        while(a is not None):
            yield a.element()
            a = self.after(a)
