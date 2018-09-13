#! /usr/bin/env python3

import string

dl_map = dict(zip(map(lambda x: str(x), range(1,27)),
                  string.ascii_lowercase[:27]))

def decode(input_s, result):
    """ decode :: string -> list -> list """
    if (len(input_s) == 0):  #consumed input
        return result
    elif (len(input_s) == 1): 
        return decode('', list(map(lambda x: x + dl_map.get(input_s), result)))
    elif (len(input_s) == 2):
        if (dl_map.get(input_s) is not None):
	    # result is processing string length of 2 and then also process string of 1
            Len2_r = decode('', list(map(lambda x: x + dl_map.get(input_s), result)))
            Len1_r = decode(input_s[1:], list(map(lambda x: x + dl_map.get(input_s[0]), result)))
            return Len2_r + Len1_r
        else:
            return decode(input_s[1:], list(map(lambda x: x + dl_map.get(input_s[0]), result)))
    else:
        R1 = decode(input_s[1:], list(map(lambda x: x + dl_map.get(input_s[0]), result)))
        R2 = decode(input_s[2:], list(map(lambda x: x + dl_map.get(input_s[:2]), result)))
        return R1 + R2

def main():
    print(decode('', ['']))
    print(decode('1', ['']))
    print(decode('12', ['']))
    print(decode('121', ['']))
    print(decode('12126', ['']))
    
if __name__ == '__main__':
    main()
