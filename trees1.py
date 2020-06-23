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

class BinaryTree(TreeBaseClass):
    def left(self,p):
        raise NotImplementedError("needs to be implemented by other classes")

    def right(self, p):
        raise NotImplementedError("needs to be implemented by other classes")
    
    def sibling(self,p):
        parent=self.parent(p)
        statement=False
        if parent is None:
            return False

        elif(self.num_children(parent)<2):
            return None
        else:
            if(p==self.left(parent)):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self,p):
        if (self.left(p)!=None):
            yield self.left(p)
        if(self.right(p)!=None):
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    '''Linked Binary Tree Exception'''
    #internal node class
    class _Node:
        __slots__ = '_element','_parent','_left','_right'
        def __init__(self,element,parent,left,right):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    #internal position class
    class Position(BinaryTree.Position):
        
        def __init__(self,container,node):
                self._container=container
                self._node=node

        def element(self):
            return self._node._element
        
        def __eq__(self,other):
            statement=False
            if(type(self)==type(other)):
                if(self._node==other._node):
                    statement=True
            return statement
            
        def __ne__(self,other):
            statement = True
            if(type(self) == type(other)):
                if(self._node == other._node):
                    statement = False
            return statement
    #internal methods
    
    def _validate(self,p):
        '''returns the node in the position after validation'''
        if not(isinstance(p,self.Position)):
            raise TypeError("p has to be a postion type")
        if(p._container is not self):
            raise ValueError("p is not of this instance ADT")
        if(p._node._parent is p._node):
            '''indirectly it is the right type of none we are looking for'''
            raise ValueError("p is not valid structure as it is over completely")
        return p._node
    
    def _make_position(self,node):
        return self.Position(self,node)
    #init method
    def __init__(self):
        self._root=None
        self._size=0
    #base methods
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    #base pos methods
    def root(self):
        '''return roots position var'''
        return self._make_position(self._root)
    def parent(self,p):
        '''give the parent's position with the child's position p'''
        node=self._validate(p)
        parent_node=node._parent
        return self._make_position(parent_node)
    def left_child(self,p):
        '''give the position of the left child of the parent which has a position p or None if no left child'''
        node=self._validate(p)
        left_child=node._left
        return self._make_position(left_child)
    def right_child(self,p):
        '''give the position of the left child of the parent which has a position p or None if no left child'''
        node = self._validate(p)
        right_child = node._right
        return self._make_position(right_child)
    def num_children(self,p):
        '''returns the number of children which has a parent position p'''
        node = self._validate(p)
        cnt=0
        if(node._left!=None):
            cnt+=1
        if(node._right!=None):
            cnt+=1
        return cnt
    #element manipulation methods
    def add_root(self,e):
        '''add element e to root of this tree and return the position of the root'''
        if(self._root is not None):
            raise ValueError("root created.")
        self._root=self._Node(e,None,None,None)
        self._size=1
        return self.root()
    def add_left(self,p,e):
        '''Adds value of e to the left child ofthe parent node with position p and returns the left child's position'''
        node=self._validate(p)
        if(node._left is not None):
            raise ValueError("left child already exists")
        else:
            self._size+=1
            node._left=self._Node(e,node,None,None)
            left_node=node._left
            return self._make_position(left_node)
    def add_right(self,p,e):
        '''Adds value of e to the left child ofthe parent node with position p and returns the left child's position'''
        node = self._validate(p)
        if(node._right is not None):
            raise ValueError("right child already exists")
        else:
            self._size += 1
            node._right = self._Node(e, node, None, None)
            right_node = node._right
            return self._make_position(right_node)
    def replace(self,p,e):
        '''replace element at position p with e and return old element at position p'''
        node=self._validate(p)
        old_val=node._element
        node._element=e
        return old_val
    def delete(self,p):
        '''delete node at position p and replace it with it's children under specific cases:
           if the num of children are two show some frickin error
           if p is invalid show some frickin error
           if it is just one just add it

           if everything goes fine, return the element that had been removed under position p     
        '''
        node=self._validate(p)
        if(self.num_children(p)==2):
            raise ValueError("The number of childrenm can't be two.It can only be one.")
        else:
            if(self.num_children(p)==0):
                self._size-=1
                node_rep=self._Node(None,None,None,None)
                old_val=node._element
                node=node_rep
                return old_val
            if(self.num_children(p)==1):
                if(node._left is not None):
                    left_node=node._left
                    left_node._parent=node._parent
                    self._size-=1
                    node_rep = self._Node(None, None, None, None)
                    old_val = node._element
                    node = node_rep
                    node._parent=node
                    return old_val
                if(node._right is not None):
                    right_node = node._right
                    right_node._parent = node._parent
                    self._size -= 1
                    node_rep = self._Node(None, None, None, None)
                    old_val = node._element
                    node = node_rep
                    node._parent=node
                    return old_val
##############################################################################
#traversals
    def visit(self,p):
        a=self._validate(p)
        return p

    def preorder_traversal(self,p):
        
        yield self.visit(p)
        node=self._validate(p)
        
        if(node._left is not None):
            left_pos=self._make_position(node._left)
            yield preorder_traversal(left_pos)
        
        if(node._right is not None):
            right_pos = self._make_position(node._right)
            yield preorder_traversal(right_pos)
    
    def postorder_traversal(self,p):
        node=self._validate(p)
        
        if(node._left is not None):
            left_pos = self._make_position(node._left)
            preorder_traversal(left_pos)

        if(node._right is not None):
            right_pos = self._make_position(node._right)
            preorder_traversal(right_pos)
        
        self.visit(p)

    def inorder_traversal(self,p):
        node=self._validate(p)

        if(node._left is not None):
            left_pos = self._make_position(node._left)
            preorder_traversal(left_pos)

        self.visit(p)

        if(node._right is not None):
            right_pos = self._make_position(node._right)
            preorder_traversal(right_pos)
    
    def positions(self,a):
        if(a=="preorder"):
            yield self.preorder_iterator_init()
        if(a=="postorder"):
            yield self.postorder_iterator_init()
        if(a=="inorder"):
            yield self.inorder_iterator_init()
        else:
            return ValueError("Wrong mode selected")
    def __iter__(self):
        #get iteration of all elements of the tree in preorder
        for p in self.positions("preorder"):
            yield p._element
    def iter(self,a):
        if(a=="preorder"):
            for p in self.positions("preorder"):
                yield p._element
        if(a=="postorder"):
             for p in self.positions("postorder"):
                yield p._element
        if(a=="inorder"):
             for p in self.positions("inorder"):
                yield p._element
    ############################################################
    #init traversal functions
    ############################################################
    
    def preorder_iterator_init(self):
        if(self._root is not None):
            for a in self.preorder_traversal(self._root):
                yield a
        else:
            return TypeError("Empty tree")
    def postorder_iterator_init(self):
        if(self._root is not None):
            for a in self.postorder_traversal(self._root):
                yield a 
        else:
            return TypeError("Empty tree")
    def inorder_iterator_init(self):
        if(self._root is not None):
            for a in self.inorder_traversal(self._root):
                yield a
        else:
            return TypeError("Empty tree")
    def list_return(self,a):
        ans_list=[]
        if(a=="preorder"):
            for i in iter("preorder"):
                ans_list.append(i)
        if(a == "postorder"):
            for i in iter("postorder"):
                ans_list.append(i)
        if(a=="inorder"):
            for i in iter("inorder"):
                ans_list.append(i)
        return ans_list
#I didn't code for other things they were already more of it but we can add minor stuff later.
