#! /usr/bin/python3

def is_one_away(s1, s2):
    if (len(s1) > len(s2)):
        str_a = s1
        str_b = s2
    else:
        str_a = s2
        str_b = s1
        
    if (len(str_a) - 1 > len(str_b)): # more than 1 away
        return False
    
    elif (len(str_a) == len(str_b)): # check replace only
        diffs = 0
        for j in range(len(str_a)):
            if (str_a[j] != str_b[j]):
                diffs += 1
                if (diffs > 1):
                    return False
        return True
    
    else: # one away, make sure no replace
        diffs = i = j = 0
        while(i < len(str_b)):
            if (str_b[i] != str_a[j]):
                diffs += 1
                if (diffs > 1):
                    return False
                else:
                    j += 1
            else:
                j += 1
                i += 1
                
        return True

def test_oneaway():
    print('Testing is_one_away() ...')
    print('\'pale, ple\' is one away? {}'.format(is_one_away('pale', 'ple')))
    print('\'pale, bale\' is one away? {}'.format(is_one_away('pale', 'bale')))
    print('\'pale, bake\' is one away? {}'.format(is_one_away('pale', 'bake')))
    print('\'pales, pale\' is one away? {}'.format(is_one_away('pales', 'pale')))
    print('\'pales, pale\' is one away? {}'.format(is_one_away('pales', 'pale')))
    print('\'pale, paile\' is one away? {}'.format(is_one_away('pale', 'paile')))
    print('\'pales, paile\' is one away? {}'.format(is_one_away('pales', 'paile')))

def is_unique(s):
    """ Returns true if string s only has unique characters, otherwise false """
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars)-1):
        if (sorted_chars[i] == sorted_chars[i+1]):
            return False
    return True

def test_isunique():
    print('\'dog\' is unique? {}'.format(is_unique('dog')))
    print('\'lassie\' is unique? {}'.format(is_unique('lassie')))
    
def is_permutation(s1, s2):
    if (len(s1) == len(s2)):
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)

        for i in range(len(s1_sorted)):
            if (s1_sorted[i] != s2_sorted[i]):
                return False
            
        return True
    else:
        return False

def test_ispermutation():
    print('\'waterbottle\' is a permutation of \'erbottlewat\'? {}'.format(is_permutation('waterbottle', 'erbottlewat')))
    
def main():    
    test_oneaway()
    
if __name__ == '__main__':
    main()
    
