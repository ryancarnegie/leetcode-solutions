class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Final Dynamic Array solution
        # It alternates (forces the alternate with current word is 1 and 2, alternates
        # between the two.
        characters = [] # We want a dynamic array so we make an empty list here
        cur_word = 1
        a, b = 0, 0
        
        while a < len(word1) and b < len(word2):
            # Alternate between word1[a] and word2[b]
            if cur_word == 1:
                characters.append(word1[a]) # O(1) where n is the length of its current string
                a += 1
                cur_word = 2
            else:
                characters.append(word2[b]) # this makes them a dynamic array
                b += 1
                cur_word = 1

        while a < len(word1):
            characters.append(word1[a])
            a += 1
        
        while b < len(word2):
            characters.append(word2[b])
            b += 1

        print(characters)
        return ''.join(characters) # O(T) - it's a string builder pattern, so we
        # 

        # Let A be the length of word1
        # Let B be the length of word2
        # Let T = A + B

        # Time: O(T)
        # Space: O(T)
