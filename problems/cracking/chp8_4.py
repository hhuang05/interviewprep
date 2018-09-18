#!/usr/bin/env python3

# 1. Change the representation from lists to strings
# 2. Use a dictionary in the final result instead of a list
# to check for duplicates

# set_S now a string, but we can still slice
# final_result is a dictionary
def power_set_help(set_S, final_result):
    if (len(set_S) == 0):
        if (final_result.get(set_S) is None):
            final_result[set_S] = 1
            
    else:
        if (final_result.get(set_S) is None):
            final_result[set_S] = 1
            
        for i in range(len(set_S)):
            newset = set_S[0:i] + set_S[i+1:len(set_S)] # excludes i
            power_set_help(newset, final_result)
	
    return final_result

def power_set(S):
    inter_result = power_set_help(S, {})
    final = []
    for k,v in inter_result.items():
        final.append(k)

    return final
    
def main():
    S = ''
    print('S = {}'.format(S))
    print('Powerset of S = {}'.format(power_set(S)))

    S = 'a'
    print('S = {}'.format(S))
    print('Powerset of S = {}'.format(power_set(S)))

    S = 'ab'
    print('S = {}'.format(S))
    print('Powerset of S = {}'.format(power_set(S)))

    S = 'abc'
    print('S = {}'.format(S))
    print('Powerset of S = {}'.format(power_set(S)))


if __name__ == '__main__':
    main()
