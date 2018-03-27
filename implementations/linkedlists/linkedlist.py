#!/usr/bin/env python3
# Writing this for python 3

class LLError(Exception):
    """Exception raised by the linked list

    Attributes:
        message -- explanation the error
    """
    def __init__(self, message):
        self.message = message
    
class LLNode:
    '''Class for Linked list node'''
    
    def __init__(self, value):
        self.key = value
        self.next = None
        
class LinkedList:
    '''Class for linked list'''
    
    def __init__(self):
        '''Default Constructor'''
        self.length = 0
        self.head = None

    def size(self):
        return self.length

    def empty(self):
        return self.length == 0

    def push_front(self, value):
        newNode = LLNode(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def front(self):
        if self.length == 0:
            return None
        else:
            return self.head.key

    def pop_front(self):
        if self.length == 0:
            return None
        else:
            rmNode = self.head
            self.head = self.head.next #update pointer
            self.length -= 1
            return rmNode

    def printList(self):
        if self.length == 0:
            print('{ }')
        else:
            str = '{ '
            start = self.head
            while start is not None:
                str += '{} '.format(start.key)
                start = start.next
            str += '}'
            print(str)

    def push_back(self, value):
        if self.length == 0:
            self.push_front(value)
        else:
            curNode = self.head
            nextNode = curNode.next
            while nextNode is not None:
                curNode = nextNode
                nextNode = nextNode.next

            # Now we're at the end
            curNode.next = LLNode(value)
            self.length += 1

    def insert(self, index, value):
        """Inserts value @ index into the linked list and returns a Boolean
        
        Assumes that items in linked lists are zero-indexed.
        index -- The index to insert into
        value -- The value of the item
        """
        if index > self.length:
            raise LLError('Index greater than the size of the list')
        elif index < 0:
            raise LLError('Index can not be negative')
        elif index == 0:
            self.push_front(value)
            return True
        elif index == self.length:
            self.push_back(value)
            return True
        else: #Now we have an index in the middle of the list
            startInd = 0
            curNode = self.head
            while startInd < index - 1:
                startInd += 1
                curNode = curNode.next

            # Now the pointer points to the node right before the
            # one we need to insert
            newNode = LLNode(value)
            newNode.next = curNode.next
            curNode.next = newNode
            self.length += 1
            return True
            
    def reverse(self):
        """Reverse the linked list in place"""

        stack = []
        curNode = self.head
        while curNode is not None:
            stack.append(curNode)
            curNode = curNode.next

        counter = 0
        self.head = stack.pop()
        runner = self.head
        while len(stack) > 0:
            runner.next = stack.pop()
            runner = runner.next #Update the runner

        # Make sure that the last item's link is nulled out, otherwise
        # will create cycles
        runner.next = None 
