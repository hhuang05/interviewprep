#!/usr/bin/env python3
# Problem: Given a root of a binary tree, 
# implement serialize(root) and deserialize(s) to serialize the tree into a string
# and turn it back into a tree

# Given the following definition of Node:

class Node:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The following tests should pass
# Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(s)).left.left.val == 'left.left'

def serialize(root):
    if (root is None):
        return ''
    else:
        template = '({},{},{})'
        if (root.left is not None and root.right is not None):
            return template.format(root.val,
                                   serialize(root.left), serialize(root.right))
        elif (root.left is None):
            return template.format(root.val, '', serialize(root.right))
        elif (root.right is None):
            return template.format(root.val, serialize(root.left), '')
        else:
            return template.format(root.val, '', '')
            


def deserialize(s):
    return Node(s)

def main():
    tree = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(tree))

if __name__ == '__main__':
    main()
