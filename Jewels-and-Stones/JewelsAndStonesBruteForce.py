class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

Time : O(M * N)
Space : O(1)

Outer loop (for stone in stones): 𝑁
Inner loop (for jewel in jewels or if stone in jewels): 𝑀

M⋅N because:
M corresponds to jewels, which is the smaller collection in most cases, and
N corresponds to stones, which is usually the larger collection.

M⋅N emphasizes the relationship between the smaller and larger input sizes. It doesn't change the actual complexity.
