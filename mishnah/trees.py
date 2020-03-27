'''rather than implementing our own tree data structure from scratch, 
   we can simply use the anytree library. 

   See: https://anytree.readthedocs.io/en/latest/api.html for the API,

   We will use this data strucutre to explain Mishnayot, such as the first in Ketubut.
   
   Install by running pip install anytree. 
   
   To save human-friendly images of the trees, run the following command: 
   
   sudo apt install graphviz.
   
   The following is a simple demonstration involving a tree with one root that has two children:
'''

from anytree import Node, RenderTree
from anytree.exporter import DotExporter   
from queue import Queue


class BinaryTree:
    def __init__(self, value):
         '''each node starts out with no children'''
         self.value = value
         self.left_child = None
         self.right_child = None

    def insert_left(self, value):
        '''inserts a BinaryTree object initialized to `value` as the left child of the current node'''
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        # if there is already a left child, then move it down in the tree to become a grandchild
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        '''inserts a BinaryTree object initialized to `value` as the right child of the current node'''
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        # if there is already a right child, then move it down in the tree to become a grandchild
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    '''traversal methods'''
    
    def pre_order(self):
        # print the root value first
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()


        # print the root value in the middle
        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.in_order()

        if self.right_child:
            self.right_child.in_order()

        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                 queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)

'''root = BinaryTree(11)
root.insert_left(8)
root.insert_right(16)
left_subtree = root.left_child
right_subtree = root.right_child
left_subtree.insert_left(5)
left_subtree.insert_right(10)
right_subtree.insert_right(18)'''

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        '''given a `value`, inserts a new node into the tree initialized to that value'''
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        '''returns True if a node with given `value` exists, False otherwise'''
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def remove_node(self, value, parent=None):
        '''deletes node with given `value` from the tree, 
           and reorganizes the tree to maitain 
           the binary search tree property. 
           `parent` is used for removal via recursion.
           returns True if the node is found and removed, False otherwise.
        '''
        # search for the node that has the value we are looking for. 
        # search the appropriate subtree depending on how value compares to the value in the current node.
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
         return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        # removal logic
        else:
            # node has no children and is the left child of its parent
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            # node has no children and is the right child of its parent
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            # node has only a left child and is the left child of its parent
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            # node has only a left child and is the right child of its parent
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            # node has only a right child and is the left child of its parent
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            # node has only a right child and is the right child of its parent
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            # node has both left and right children
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        '''sets value and children of current node to None'''
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        '''returns the minimum value in the tree'''
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    '''traversal methods'''

    def pre_order(self):
        # print the root value first
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            yield from self.left_child

        yield self.value

        if self.right_child:
            yield from self.right_child
    
    def __iter__(self):
        return (x for x in self.in_order())
        
        # if self.left_child:
        #     self.left_child.in_order()
        
        # # print the root value in the middle
        #     print(self.value)
        
        # if self.right_child:
        #     self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.in_order()

        if self.right_child:
            self.right_child.in_order()

        # print the root value last
        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                 queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)

class ListClass:
    def __init__(self, ls=[]):
        self.items = ls
    def append(self,item):
        self.items = self.items + [item]

    def __iter__(self):
        return (item for item in self.items)

if __name__ == "__main__":
    # wire up the nodes to each other, making a linked structure
    root = Node("root")
    left_child = Node("left_child", parent=root)
    right_child = Node("right_child", parent=root)

    print(root.children)

    # print out a representation of the tree on the commmand line
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    # save an image of the tree starting from the root in the current working directory called 'root.png'
    DotExporter(root).to_picture("root.png")