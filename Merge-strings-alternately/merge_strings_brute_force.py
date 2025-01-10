class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Final Brute Force solution
        characters = ''
        cur_word = 1
        a, b = 0, 0
        
        while a < len(word1) and b < len(word2):
            # Alternate between word1[a] and word2[b]
            if cur_word == 1:
                characters += word1[a]
                a += 1
                cur_word = 2
            else:
                characters += word2[b]
                b += 1
                cur_word = 1

        while a < len(word1):
            characters += word1[a]
            a += 1
        
        while b < len(word2):
            characters += word2[b]
            b += 1

        return characters

        # Let A be the length of word1
        # Let B be the length of word2
        # Let T = A + B

        # Time: O(T^2)
        # Space: O(T)

        
