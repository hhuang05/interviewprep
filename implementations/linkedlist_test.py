#!/usr/bin/env python3

from linkedlist import LinkedList


def main():
    newlist = LinkedList()
    newlist.push_back(3)
    newlist.push_back(5)
    newlist.push_back(8)
    newlist.push_back(5)
    newlist.push_back(10)
    newlist.push_back(2)
    newlist.push_back(1)
    newlist.push_back(4)
    newlist.push_back(3)
    newlist.printList()

    ch2_4(newlist, 5)
    newlist.printList()
    
# This check is here to make sure that specific code can only
# be run when this script is run by itself. During imports where the
# main function could also be run, this prevents it. 
if __name__ == '__main__':
    main()
else:
    print('I\'m being imported')
