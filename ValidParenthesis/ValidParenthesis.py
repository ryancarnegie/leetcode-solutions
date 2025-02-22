class Solution:
    def isValid(self, s: str) -> bool:
        h = { ')':'(', ']':'[', '}':'{' } # h be a hashmap with key:value pairs as (closing bracket, open bracket), O(1) and (n) respectively.
        stack = [] # stack be an empty stack

        for bracket in s: # we are looking for brackets in the string of s
            if bracket not in h:
                stack.append(bracket)
            else:
                if not stack:
                    return False # close for no prev. open
                elif stack.pop() != h[bracket]:
                    return False # mismatch/wrong order
        if not stack:
            return True
        else:
            return False # beginning open bracket
        
        # Time: O(n)
        # Space: O(n)
  
