class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = nums[0]
        for num in nums:
            if num < mins:
                minn = num
        return minn        

        # Time: O(n)
        # Space: O(1)
