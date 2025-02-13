class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        array = []
        for i in range(len(s) - 1, -1, -1):
            array.append(s[i])
        for i in range(len(s)):
            s[i] = array[i]
        return None

# Time: O(n)
# Space: O(n)
