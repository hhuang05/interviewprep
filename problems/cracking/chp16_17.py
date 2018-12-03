#!/usr/bin/env python3

def calc_cursum(pos_indices, seq):
    cur_sum = 0
    if len(pos_indices) > 0:
        for k in pos_indices:
            cur_sum += seq[k]
        cur_sum += seq[k+1]

    return cur_sum
        
def largest_sum(seq):
    deltas = []
    for i in range(len(seq)-1):
        deltas.append(seq[i] + seq[i+1])

    print(deltas)
    # Look through deltas
    pos_indices = []
    max_sum = 0
    for j, v in enumerate(deltas):
        if (v > 0):
            pos_indices.append(j)
        else:
            cur_sum = calc_cursum(pos_indices, seq)
            if (cur_sum > max_sum):
                max_sum = cur_sum
            pos_indices.clear()

    cur_sum = calc_cursum(pos_indices, seq)
    if (cur_sum > max_sum):
        max_sum = cur_sum
            
    return max_sum

def main():
    # seq = [2, -8, 3, -2, 4, -10]
    # print(seq)
    # print('Largest sum is: {}'.format(largest_sum(seq)))

    seq = [5, -1,  8, -15, 9, -4, 6] 
    print(seq)
    print('Largest sum is: {}'.format(largest_sum(seq)))


if __name__ == '__main__':
    main()
