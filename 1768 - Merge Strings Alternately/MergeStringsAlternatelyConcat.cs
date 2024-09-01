public class Solution {
    public string MergeAlternately(string word1, string word2) {
        string result = "";
        for (int i = 0; i < word1.Length || i < word2.Length; i++) {
            if (i < word1.Length) {
                result += string.Concat(word1[i]);
            }
            if (i < word2.Length) {
                result += string.Concat(word2[i]);
            }
        }
        return result;
    }
}
