#!/usr/bin/env python3
# Writing this for python 3

class LinkedList:
    '''Class for linked list'''
    
    def __init__(self):
        self.length = 0
        self.head = None

    def size(self):
        return self.length

    def empty(self):
        return self.length == 0
    
