#!/usr/bin/env python3

# Problem: Given a list of integers and k, return if there exists
# a pair of numbers in the list that adds up to k.

# Assume there may be repeats and not sorted
# O(n) solution
#  ~ roughly 2n

def solution(arr, k):
    ''' Returns the two numbers as a tuple from the list which adds 
        up to k
    '''

    checkNum = dict()
    for num in arr:
        if (checkNum.get(num) is None):
            checkNum[num] = 1
        else:
            checkNum[num] += 1

    print(checkNum)
    for key in checkNum.keys():
        num2 = k - key
        v2 = checkNum.get(num2)
        if (v2 is not None):
            return (key, num2)

    return None

def main():
    arr = [10, 15, 3, 7]
    k = 16
    print(solution(arr, k))

    
if __name__ == '__main__':
    main()
