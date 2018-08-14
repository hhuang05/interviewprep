#!/usr/bin/env python3
# Specifically designing this for python3

"""
Operations of stacks are:

push(item) - pushes the item onto the stack
pop() - returns the last item on the stack, modifies the stack
peek() - Looks at the last item, doesn't modify
isEmpty() - checks to see if stack is empty
numItems() - Returns the number of items in the stack
"""

class Stack:
    """ The stack class """

    def __init__(self):
        """ Default constructor """
        self.num_items = 0 # Can not be negative
        self.the_stack = []
        
    def isEmpty(self):
        return self.num_items == 0

    def numItems(self):
        return self.num_items

    def peek(self):
        """ Looks at the first item in the stack """
        if self.isEmpty() is False:
            return self.the_stack[-1]

    def push(self, item):
        """ Pushes the item onto the stack """
        self.the_stack.append(item)
        self.num_items += 1
        return self.num_items

    def pop(self):
        """ Returns the first item in the stack """
        if self.isEmpty():
            return None
        else:
            self.num_items -= 1
            return self.the_stack.pop()
