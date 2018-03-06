#!/usr/bin/env python3
# Writing this for python 3

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
