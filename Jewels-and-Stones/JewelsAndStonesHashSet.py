# Brute Force Solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count
Time: O(M + N)
Space: O(N) because it is turning that string into a {set} of jewels. That set will hold the same amount of space as the stuff its storing. 


# Optimal Solution
# Modified version
# You make s a set of jewels to enable efficient membership checking. Sets in Python provide 
# O(1) average-time complexity for lookups, which makes checking whether a stone is a jewel much faster 
# compared to iterating through a list of jewels (which would take O(M) for each lookup). 
# This optimization significantly improves performance.
    count = 0
    jewels_set = set(jewels)
    for stone in stones:
        if stone in jewels_set:
            count += 1
    return count
