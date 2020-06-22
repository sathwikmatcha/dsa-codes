class TreeBaseClass:
    '''This class is a base class which is going to used for further inheritance'''
    class Position:
        def element(self):
            raise NotImplementedError("needs to be implemented by other classes")
        def __eq__(self):
            raise NotImplementedError("needs to be implemented by other classes")
        def __ne__(self):
            raise NotImplementedError("needs to be implemented by other classes")

    def root(self):
        raise NotImplementedError("needs to be implemented by other classes")
    def parent(self,p):
        raise NotImplementedError("needs to be implemented by other classes")
    def children(self,p):
        raise NotImplementedError("needs to be implemented by other classes")
    def __len__(self):
        raise NotImplementedError("needs to be implemented by other classes")
    def num_children(self,p):
        raise NotImplementedError("needs to be implemented by other classes")
    def is_root(self,p):
        return self.root()==p
    def is_leaf(self,p):
        return self.num_children()==0
    def is_empty(self):
        return len(self)==0