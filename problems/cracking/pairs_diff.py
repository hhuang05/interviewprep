#! /usr/bin/env python3


def pairs_difference(in_array, k):
    if (len(in_array) <= 1):
        return 0

    if (type(k) is not int):
        print('k must be integer')
        return 0
    else:
        num_pairs = 0
        s_array = sorted(in_array) #sorts it in place
        anchor = 0
        runner = 1
        while (anchor < len(s_array)-1 and
               runner < len(s_array)) :
            diff = s_array[runner] - s_array[anchor] 
            if (diff < k):
                runner += 1
            else:
                if (diff == k):
                    num_pairs += 1
                anchor += 1
                runner = anchor + 1

        return num_pairs

def main():
    s = [1, 7, 5, 9, 2, 12, 3]
    k = 2
    print(s,k)
    print(pairs_difference(s, k))

    s = [1, 7, 5]
    k = 3
    print(s,k)
    print(pairs_difference(s, k))

    s = [2]
    k = 3
    print(s,k)
    print(pairs_difference(s, k))

if __name__ == '__main__':
    main()
