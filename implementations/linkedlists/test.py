#!/usr/bin/env python3

from linkedlist import LinkedList

def main():
    newlist = LinkedList()
    newlist.push_front(2)
    newlist.push_front(5)
    newlist.printList()
    newlist.push_back(3)
    newlist.printList()
    newlist.insert(-1, 6)
    newlist.printList()

# This check is here to make sure that specific code can only
# be run when this script is run by itself. During imports where the
# main function could also be run, this prevents it. 
if __name__ == '__main__':
    main()
else:
    print('I\'m being imported')
