class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        h = {} # let h be an empty hash map
        for i in range(n):        # n x 
            x = nums[i]
            y = target - x
            if y in h:            # O(1)
                return [i, h[y]]
            else:
                h[x] = i  # this makes it so h[x] is the key and i is the value

              
        # Time : O(n)
        # Space : O(n)

        # We use some more space in the optimal solution but we do this because
        # it allows us to use a different data structure to do something more
        # efficiently. We will take that tradeoff every time.
