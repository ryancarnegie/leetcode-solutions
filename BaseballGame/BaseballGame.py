class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            if item == '+':
                stack.append(stack[-1] + stack[-2])
            elif item == 'D':
                stack.append(stack[-1] * 2)
            elif item == 'C':
                stack.pop()
            else:
                stack.append(int(item))
        return sum(stack)

# Time: O(n)
# Space: O(n)

It can't go faster than O(n) time because we have to loop through things. 
