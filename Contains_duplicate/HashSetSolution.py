Hashset
Time: O(N)
Space: O(N)

def contains_duplicate_set(nums):
    empty_set = set()
    n = len(nums)
    for x in range(n):
        if nums[x] in empty_set:
            return True
        else:
            empty_set.add(nums[x])
    return False

