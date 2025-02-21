class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1

        while l <= r:
            mid = (l + r) // 2
            mid_i = mid // n
            mid_j = mid % n
            midNum = matrix[mid_i][mid_j]
            if target == midNum:
                return True
            elif target < midNum:
                r = mid - 1
            else:
                l = mid + 1
        return False

        # Time: O(log(m * n))
        # Space: O(1)

