#! /usr/bin/env python3

def long_consec_char(input_s):
    if (input_s == ''):
        return {'' : 0}

    cur_count = 0
    max_count = 0
    max_char = ''
    prev_char = ''
    for s in input_s:
        if (prev_char == ''):
            cur_count = 1
        elif (s == prev_char):
            cur_count += 1
        else:
            if (max_count < cur_count):
                max_count = cur_count
                max_char = prev_char

            cur_count = 1

        prev_char = s

    # Last check in case we have character at the end
    if (max_count < cur_count):
        max_count = cur_count
        max_char = prev_char
        
    return {max_char: max_count}

def main():
    s = 'ABBCDDEEBBBB'
    print(s)
    print(long_consec_char(s))
    
if __name__ == '__main__':
    main()
