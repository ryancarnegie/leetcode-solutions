class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count

Time: O(N + M)
Space: O(N) because it is turning that string into a {set} of jewels. That set will hold the same amount of space as the stuff its storing. 
