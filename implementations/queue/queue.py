#!/usr/bin/env python3
# Writing specifically for python3

"""
Queue - First in, First Out

Operations:

enqueue(item):
dequeue()
full(): Boolean
empty() : Boolean

"""

class Queue:

    def __init__(self):
        """ Creates an empty queue """
        self.num_items = 0
        self.the_queue = []
        self.head
