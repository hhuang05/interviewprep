#!/usr/bin/env python3

from linkedlist import LinkedList

def main():
    newlist = LinkedList()
    print('List length {0}'.format(newlist.size()))
    print('List is empty? {0}'.format(newlist.empty()))
    
if __name__ == '__main__':
    main()
