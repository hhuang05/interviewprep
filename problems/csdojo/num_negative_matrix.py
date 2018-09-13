#! /usr/bin/env python3

def count_negnum(M):
    rows= len(M)

    if (rows == 0):
        return 0
    elif (type(M[0]) is int):
        return 1 if M[0] < 0 else 0        

    cols = len(M[0])
    neg_nums = 0
    i = 0
    while (i < rows):
        j = 0
        while (j < cols):
            if (M[i][j] < 0):
                neg_nums += 1
                j += 1
            else:
                cols = j
                i += 1
                
        if (cols == 0):
            break
        
    return neg_nums

def main():
    M = [[-3, -2, -1, 1],
         [-2, 2, 3, 4],
         [4, 5, 7, 8]]
    print(M)
    print(count_negnum(M))

    M = [[-1, 2],
         [3, 5]]
    print(M)
    print(count_negnum(M))

    M = [-1,2]
    print(M)
    print(count_negnum(M))

if __name__ == '__main__':
    main()
