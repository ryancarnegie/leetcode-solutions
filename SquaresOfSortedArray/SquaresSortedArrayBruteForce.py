class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] =  nums[i] ** 2
        nums.sort()
        return nums


# Time: O(n log n) because of the sorting algorithm, otherwise it would be log(n)
# Space: O(1)  not storing anything

