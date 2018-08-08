#!/usr/bin/env python3

def plusOne(digits):
    if len(digits) == 0:
        return []
    
    ones_index = len(digits)-1

    for i in range(ones_index, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0

    if digits[0] == 0:
        digits.insert(0,1)

    return digits

def main():
    print(plusOne(['a']))
    print(plusOne([1]))
    print(plusOne([9]))
    print(plusOne([1,9]))
    print(plusOne([9,9]))
    print(plusOne([9,9,8]))
    print(plusOne([9,9,9]))

main()
    
    
    
    
    
