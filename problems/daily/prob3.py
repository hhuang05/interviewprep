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

# Invariant is that at the end of deserialize, that the root node should be
# on the process stack
def deserialize(s):
    process_stack = []
    cur_node_val = ''
    for c in s:
        if c == '(':
            continue
        
        elif c == ')':
            rightNode = Node(cur_node_val)
            cur_node_val = ''
            leftNode = process_stack.pop()
            rootNode = process_stack.pop()
            rootNode.left = leftNode
            rootNode.right = rightNode
            process_stack.append(rootNode)

        elif c == ',':
            newNode = Node(cur_node_val)
            cur_node_val = ''
            process_stack.append(newNode)
            
        else:
            cur_node_val += c

    if len(process_stack) == 1:
        return process_stack.pop()

    print(process_stack)
    
    return None

def main():
    tree = Node('root', Node('left', Node('left.left')), Node('right'))
    serializedTree = serialize(tree)
    testTree = '(root,(left,(left.left,,),),(right,,))'
    print(deserialize(testTree))

if __name__ == '__main__':
    main()
