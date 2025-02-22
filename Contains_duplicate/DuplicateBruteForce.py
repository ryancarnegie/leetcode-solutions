class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if nums[x] == nums[y] and x != y: # Don't need x != y check with x + 1 in second loop either
                    return True
        return False

# Time: O(N^2)
# Space: O(1)
# Very inefficient, will exceed time limits in some circumstances
