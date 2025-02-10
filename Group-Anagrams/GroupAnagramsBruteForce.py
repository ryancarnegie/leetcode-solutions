# Brute Force Solutions
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            ans[key].append(s)
        return list(ans.values())

Time: O(n * m log m)
# Space: O(n * m)


# Explanation:
# The defaultdict turns the if/else statement into a one liner.
# If it is not a defaultdict, it would be:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
        return list(ans.values())
