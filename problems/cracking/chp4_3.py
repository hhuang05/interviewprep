#!/usr/bin/env python3

"""
Operations
- insert // insert value into tree
- get_node_count // get count of values stored
- print_values // prints the values in the tree, from min to max
    - in order
    - pre order
    - post order
- delete_tree
- is_in_tree // returns true if given value exists in the tree
- get_height // returns the height in nodes (single node's height is 1)
- get_min // returns the minimum value stored in the tree
- get_max // returns the maximum value stored in the tree
- delete_value
- get_successor // returns next-highest value in tree after given value, -1 if none
- get_predecessor //returns the next-highest value in tree before given value, -1 if none
"""

class BSTNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.key = value
        self.parent = None
        self.depth = 0

    def visit_node(self, result):
        """
        Assume that result is a dictionary with k = key, value is the list of nodes
        """
        if self.key is None:
            return

        if (result.get(self.depth) is None):
            result[self.depth] = []
            
        result[self.depth].append(self)

        if (self.left is not None):
            self.left.visit_node(result)

        elif (self.right is not None):
            self.right.visit_node(result)

    def inOrderTraversal(self, fun):
        if (self.left is not None):
            self.left.inOrderTraversal(fun)

        fun(self)

        if (self.right is not None):
            self.right.inOrderTraversal(fun)

    def printInOrder(self):
        if (self.left is not None):
            self.left.printInOrder()

        print('{} '.format(self.key))

        if (self.right is not None):
            self.right.printInOrder()

    def printPreOrder(self):
        print('{} '.format(self.key))
        
        if (self.left is not None):
            self.left.printInOrder()

        if (self.right is not None):
            self.right.printInOrder()

    def printPostOrder(self):        
        if (self.left is not None):
            self.left.printInOrder()

        if (self.right is not None):
            self.right.printInOrder()

        print('{} '.format(self.key))

class BST:

    def __init__(self, root):
        self.root = root
        self.num_items = 1

    def printInOrder(self):
        print('In order traversal')
        self.root.printInOrder()

    def printPreOrder(self):
        print('Pre order traversal')
        self.root.printPreOrder()

    def printPostOrder(self):
        print('Post order traversal')
        self.root.printPostOrder()
        
    def insert(self, value):
        """Inserts new node into the tree"""
        newNode = BSTNode(value)

        start = self.root
        cur_depth = self.root.depth
        while start is not None:
            y = start
            if value < start.key:
                start = start.left
            else:
                start = start.right

        # We found the parent node after this
        # Now update tree        
        newNode.parent = y
        if value < y.key:
            y.left = newNode
        else:
            y.right = newNode

        newNode.depth = newNode.parent.depth + 1
                       
    def minimum(self):
        x = self.root
        print(x.key)
        while x is not None:
            x = x.left
        return x

def main():
    newRoot = BSTNode(5)
    newTree = BST(newRoot)

    newTree.insert(6)
    newTree.insert(3)
    newTree.insert(4)    
    newTree.insert(10)    
    newTree.insert(8)
    newTree.insert(9)
    newTree.insert(11)

    newRoot.inOrderTraversal(lambda x: print('Depth: ' + str(x.depth)))
    result = dict()
    newRoot.inOrderTraversal(lambda x:
                             x.depth)))
    newRoot.visit_node(result)
    print(result)

if __name__ == '__main__':
    main()
