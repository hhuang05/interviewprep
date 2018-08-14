#!/usr/bin/env python3

def strStr2(source, target):
    for i in range(len(source) - len(target) + 1):
        for j in range(len(target)):
            print('Source {0}, Target {1}'.format(source[i+j], target[j]))
            if source[i+j] != target[j]:
                break

        if j+1 == len(target):
            return i

    return -1

def strStr(source, target):
    # write your code here
    if source is None or target is None:
        return -1
    elif len(source) == len(target) == 0:
        return 0
    elif len(target) == 0:
            return 0
    else:
        i = 0 
        while i < len(source):
            if source[i] == target[0] :
                j = 1
                    
                while j < len(target) and i+j < len(source):
                    if target[j] == source[i+j]:
                        j += 1                        
                    else:
                        i += j
                        break
                        
                if j == len(target):
                    return i # Found it!
            
            i += 1
                    
        return -1

def main():
    s = "target"
    t = "a"

    print(strStr2(s, t))

if __name__ == '__main__':
    main()
