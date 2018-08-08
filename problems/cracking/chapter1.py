#! /usr/bin/python3

def is_unique(s):
    """ Returns true if string s only has unique characters, otherwise false """
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars)-1):
        if (sorted_chars[i] == sorted_chars[i+1]):
            return False
    return True

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
    
def main():    
    print('\'dog\' is unique? {}'.format(is_unique('dog')))
    print('\'lassie\' is unique? {}'.format(is_unique('lassie')))
    print('\'waterbottle\' is a permutation of \'erbottlewat\'? {}'.format(is_permutation('waterbottle', 'erbottlewat')))
    
if __name__ == '__main__':
    main()
    
