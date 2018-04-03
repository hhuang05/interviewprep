#!/usr/bin/env python3

def swap(arr, a, b):
    tmp = arr[b]
    arr[b] = arr[a]
    arr[a] = tmp
    
def partition(arr, from_ind, to_ind):
    pivot = arr[to_ind]
    i = from_ind - 1
    for j in range(from_ind, to_ind):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, to_ind)
    return i+1

def qsort_help(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        qsort_help(arr, p, q-1)
        qsort_help(arr, q+1, r)

def quicksort(arr):
    qsort_help(arr, 0, len(arr)-1)

def main():
    a = [2,8,7,1,3,5,6,4]
    print(a)
    quicksort(a)
    print(a)
    
if __name__ == '__main__':
    main()
