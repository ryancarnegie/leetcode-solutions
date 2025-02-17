class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        result = [0] * n

        for i in range(n):
            nums[i] = nums[i] ** 2
        j = n - 1
        
        while l <= r:
            if nums[l] > nums[r]:
                result[j] = nums[l]
                l += 1
            else:
                result[j] = nums[r]
                r -= 1
            j -= 1
        return result

        # Time: O(n)
        # Space: O(n)
