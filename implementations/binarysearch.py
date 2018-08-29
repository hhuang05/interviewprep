#! /usr/bin/env python3


def binary_search(lst, target):
    L = 0
    R = len(lst)
    while (L != R):
        mid = ((R-L) // 2) + L
        if (target == lst[mid]):
            return mid
        elif (target > lst[mid]):
            L = mid + 1
        else:
            R = mid #invariant, R must be always len of search space

    return None
    
def main():
    a = [1,3,4]
    print(binary_search(a,5))
    
if __name__ == '__main__':
    main()
