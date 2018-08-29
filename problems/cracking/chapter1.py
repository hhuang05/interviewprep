#! /usr/bin/env python3

from enum import Enum
import numpy as np

class ImageSide(Enum):
    """ Different sides of image """
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

def rotateImage(data, N):
    """ Rotates a NxN image to the right by 90 degrees 

    Function Signature
       rotateImage :: ndarray -> int -> ()

    """
    if (N == 0 or N == 1):
        return
    else:    
        target_coords = []
        target_vals = []
        source_vals = []
        source_coords = []
        has_moved = dict()
        
        for side_done in ImageSide:
            # For the start we always have to build up the source coords
            # However, for each subsequent one, we don't
            if (side_done == ImageSide.TOP):
                x_start = 0
                pair = []
                for y in range(N):
                    pair.append(x_start)
                    pair.append(y)
                    source_val = data[x_start][y]
                    source_vals.append(source_val)
                    source_coords.append(pair)                 
                    pair = []

            # Now do transform on source coordinates based on
            # the side
            for s in source_coords:
                key = str(s[0]) + str(s[1])

                # If it already has been moved, skip it
                if (has_moved.get(key) is not None):
                    continue
                else:
                    has_moved[key] = s                    
                    old_s0 = s[0]
                    old_s1 = s[1]

                    if (side_done == ImageSide.TOP): # Start on top side
                        s[0] = s[1]
                        s[1] = N-1
                    elif (side_done == ImageSide.BOTTOM):
                        s[0] = s[1]
                        s[1] = 0
                    else: #LEFT or RIGHT is fine
                        y = s[1]
                        s[1] = N-s[0]-1
                        s[0] = y
                        
                    target_coords.append(s)
                    target_val = data[s[0]][s[1]]
                    target_vals.append(target_val)
                    print("Source coord: ({},{}), Target coord ({},{})".format(
                        old_s0, old_s1, s[0], s[1]))
                    

            # Write into target coordinates
            for i in range(len(target_coords)):                    
                coord = target_coords[i]                
                print("Source value: {}, overwriting {}".format(
                    source_vals[i], data[coord[0]][coord[1]]))
                data[coord[0]][coord[1]] = source_vals[i]

            # Now target_coords is the new source and we zero out the target
            intermediate = target_coords
            inter_vals = target_vals
            target_coords = []
            target_vals = []
            source_coords = intermediate
            source_vals = inter_vals
    
def test_rotateImage():
    image = np.array([[0,1,2],[3,4,5],[6,7,8]])
    rotateImage(image, 3)
    
def str_compress(s):
    """ Attempts to compress string s by reduce repeats to a count

    Examples::

       'aabbcddeeaa' --> 'a2b2c1d2e2a2'
    """
    current_char = s[0]
    output = []
    count = 0
    for c in s:        
        if (c == current_char):
            count += 1
        else:
            output.append(current_char)
            output.append(str(count))
            current_char = c
            count = 1

    # Have to account for the last char set which has been repeated
    output.append(current_char)
    output.append(str(count))
    
    no_comp = True
    for i in range(1, len(output), 2):
        if (output[i] != '1'):
            no_comp = False
            break

    if (no_comp):
        return s
    else:
        return ''.join(output)

def test_strcompress():
    print('Testing str_compress() ...')
    print('Compressing aabbcddeeaabb to {}'.format(
        str_compress('aabbcddeeaabb')))
    print('Compressing abcdefg to {}'.format(str_compress('abcdefg')))
    
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
    test_rotateImage()
    
if __name__ == '__main__':
    main()
    
