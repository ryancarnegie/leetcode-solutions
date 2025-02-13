class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # Two Pointer Solution
        n = len(s)
        l = 0
        r = len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
          
        return

        # Time: O(n)
        # Space: O(1)
