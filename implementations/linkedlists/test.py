#!/usr/bin/env python3

from linkedlist import LinkedList

def main():
    newlist = LinkedList()
    newlist.push_front(2)
    newlist.push_front(5)
    newlist.printList()
    newlist.push_back(3);
    newlist.printList()


# This is here so that if this is run as a script from shell, it starts the correct functions    
if __name__ == '__main__':
    main()
