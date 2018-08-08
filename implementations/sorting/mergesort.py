#!/usr/bin/env python3

import math

def merge(A, p, q, r):
    #print('p = {}, q = {}, r = {}'.format(p,q,r))
    # 1. Calculate lengths of two sublists
    n1 = q - p + 1 
    n2 = r - q

    # 2. Copy sublists 
    left_list = []
    right_list = []

    for i in range(0, n1):
        left_list.append(A[i + p])

    for j in range(0, n2):
        right_list.append(A[j + q + 1])

    left_list.append(math.inf)
    right_list.append(math.inf)
    
    i = j = 0 #Indices to increment left and right lists
    
    # 3. Merge
    for k in range(p,r+1):
        if (left_list[i] <= right_list[j]):
            A[k] = left_list[i]
            i += 1
        else:
            A[k] = right_list[j]
            j += 1

def mergesortHelp(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        # print('Q is {}'.format(q))
        mergesortHelp(A, p, q)
        mergesortHelp(A, q+1, r)
        merge(A, p, q, r)

def mergesort(A):
    """Performs merge sort on list A"""
    mergesortHelp(A, 0, len(A)-1)
        
def main():
    a = [2,8,7,1,3,5,6,4]
    print(a)
    mergesort(a)
    print(a)

if __name__ == '__main__':
    main()
