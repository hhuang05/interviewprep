#!/usr/bin/env python3
def binary_search(lst, target):
    L = 0
    R = len(lst)
    while (L != R):
        mid = ((R-L) // 2) + L
        if (target == lst[mid]):
            return mid
        elif (target > lst[mid]):
            L = mid + 1
        else:
            R = mid #invariant, R must be always len of search space
    return None

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
        
    if (len(nums) <= 1):
        return None
    elif (len(nums) == 2):
        if (target == nums[0] + nums[1]):
            return [0,1]
    else:
        # Create list of pairs of values and indices
        vilist = [(v,i) for i,v in enumerate(nums)]            
        vilist.sort(key=lambda x: x[0]) # Sort by the value
    
        # Extract vals
        split_list = list(zip(*vilist)) #unzip the pairing
        val_list = split_list[0]
        i_list = split_list[1]
            
        # Iterate over each pair of values and indices
        # For each pair, take target, subtract
        for j, val in enumerate(val_list):
            first_ind = i_list[j]
            search_item = target - val
            k = binary_search(val_list, search_item)
            if (k is not None):
                if (j != k):
                    second_ind = i_list[k]
                    if (first_ind > second_ind):
                        result = [second_ind, first_ind]
                    else:
                        result = [first_ind, second_ind]

                    return result

def main():
    nums = [2,9,11,15,8,10,39]
    target = 21
    print(twoSum(nums, target))
    
if __name__ == '__main__':
    main()
