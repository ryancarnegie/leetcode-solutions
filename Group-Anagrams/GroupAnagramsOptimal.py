class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {} 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
        return list(ans.values())


# Breakdown of each line.

Line 4. We're calling it answer because we're basically returning it. We're returning a list of the values of that. 
Line 4. All of the dictionary values are what we need, we need a list of those things. Ans is an empty dictionary.    
Line 5. We're looking at a string, s. We need to get its key. 
Line 6. To build it up, we make count a list 26 values, and then to build up that key, we go through that word. 
Line 7. For that word that we have, (s), we go through the letters (c) of that word (s).
Line 8. If we have a letter we need to map it to its corresponding index which we do with ord. 
We say the count at that desired index is going to go up by one. We have one more of those letters.
Line 8. If we go through all of the letters with the loop on line 7, at the end of this loop we have a key.
Line 9. At the end of the loop we have a key, it's in the form of a list, and so we need to make it a tuple so it's frozen.
Line 11. If we've seen the key before (the type of anagram), that means we've already done [s] on line 14, and make
the key be a list of that word, or one of that anagram type. If we've seen it before, great, we are going to 
append that word to the list of stuff that we've seen, otherwise need to create it.
It can be one with a defaultdict with a one liner of code.

Line 13. Returns an iterable. That means it returns a thing that you can loop through. 
But it does not return a list. It needs to return a list of all of those inner lists, the inner lists
being on line 3 in the defintion. 


Notes: If you ever see the word "grouping", you can use a dictionary. 
We group because we can map the 'like thing', the thing it shares in common will be the key, and then 
you can always group those words up together in a list of stuff.
