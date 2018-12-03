#!/usr/bin/env python3


def countingValleys(n, s):
    num_valleys = 0
    num_mts = 0
    cur_level = 0
    prev_level = 0
    
    for c in s:
        if cur_level == 0:
            if prev_level < 0:
                num_valleys += 1
            elif prev_level > 0:
                num_mts += 1
          
        prev_level = cur_level

        if c == 'D':  
            cur_level -= 1
        elif c == 'U':
            cur_level += 1

    if cur_level == 0:
        if prev_level < 0:
            num_valleys += 1
        elif prev_level > 0:
            num_mts += 1

    return num_valleys

def main():
    s = 'DDUU'
    n = len(s)
    print(s)
    print(countingValleys(n,s))

    
if __name__ == '__main__':
    main()
