#!/usr/bin/env python3

import platform
import sys
sys.path.append('../../implementations/linkedlists/')
from linkedlist import LinkedList

def partition(llist, partition):
    """ Orders a linked list according to partition

    All elements less than partition is to its left
    """
    L = R = R_prime = llist.head    
    while (R is not None):
        if (R.key < partition):
            if (L == R):
                R_prime = R # Always remember the previous R location
                R = R.next
            else:
                # Break edge from R_prime
                R_prime.next = None
                L_tmp = L.next
                L.next = R
                R_tmp = R.next
                R.next = L_tmp
                L = L.next
                R = R_tmp
                
        else:
            R_prime = R
            R = R.next
            
def test_partition():
    print('Testing partition()......')
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
    print('Input list:')
    newlist.printList()

    partition(newlist, 5)
    print('After partition:')
    newlist.printList()

def sum_lists(lst1, lst2):
    if (lst1.size() > lst2.size()):
        longlst = lst1
        shortlst = lst2
    else:
        longlst = lst2
        shortlst = lst1

    lstart = longlst.head
    sstart = shortlst.head
    carry = 0
    output = LinkedList()

    # First add according to the length of short list
    while(sstart is not None):
        result = lstart.key + sstart.key + carry
        carry = 1 if result >= 10 else 0
        result_digit = result % 10
        output.push_back(result_digit)
        sstart = sstart.next
        lstart = lstart.next

    # Now to do the rest of the long list
    while (lstart is not None):
        result = lstart.key + carry
        carry = 1 if result >= 10 else 0
        result_digit = result % 10
        output.push_back(result_digit)
        lstart = lstart.next

    # Have to factor in the last carry
    if (carry > 0):
        output.push_back(carry)
        
    return output

def test_sumlists():
    print('Testing sum_lists()......')
    list1 = LinkedList()
    list1.push_back(7)
    list1.push_back(1)
    list1.push_back(6)
    
    list2 = LinkedList()
    list2.push_back(5)
    list2.push_back(9)
    list2.push_back(2)
    
    o = sum_lists(list1, list2)
    o.printList()
    
if __name__ == '__main__':
    test_sumlists()
