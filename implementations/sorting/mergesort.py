#!/usr/bin/env python3

import math

def merge(A, p, q, r):
    print('p = {}, q = {}, r = {}'.format(p,q,r))
    # 1. Calculate lengths of two sublists
    n1 = q - p + 1 
    n2 = r - q

    # 2. Copy sublists by slicing, make room for sentinel
    left_list = A[p:q+1] # Open interval from [p,q)
    right_list = A[q+1:r]

    left_list.append(math.inf)
    right_list.append(math.inf)
    print(left_list)
    print(right_list)

    i = j = 0 #Indices to increment left and right lists
    
    # 3. Merge
    for k in range(p,r+1):
        if (left_list[i] <= right_list[j]):
            A[k] = left_list[i]
            i += 1
        else:
            A[k] = right_list[j]
            j += 1

def mergesort(A, p, r):
    if p < r:
        q = int((p + r) / 2) 
        print('Q is {}'.format(q))
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)

    
def main():
    print('merge sort')
    a = [ 1, 3, 7, 8, 2, 4]
    mergesort(a, 0, len(a)-1)
    print(a)

if __name__ == '__main__':
    main()
