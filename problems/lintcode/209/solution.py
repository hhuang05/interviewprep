#!/usr/bin/env python3

def firstUniqChar(string):
    if string == "":
        return ""
    if string is None:
        return ""
    
    countTable = dict()
    for s in string:
        try:
            countTable[s] += 1
        except:
            countTable[s] = 1

    for s in string:
        if countTable[s] == 1:
            return s

def main():
    print(firstUniqChar("abaccdeff"))
                      
main()
