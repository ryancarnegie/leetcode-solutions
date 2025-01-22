Hashset
Time: O(N)
Space: O(N)

def contains_duplicate_set(nums):
    empty_set = set()
    for x in nums:
        if x in empty_set:
            return True
        else:
            empty_set.add(x)
    return False
    
