class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_idx = 0
        word2_idx = 0
        word = ''

        while word1_idx<len(word1) and word2_idx<len(word2):
            word += word1[word1_idx]
            word += word2[word2_idx]
            word1_idx +=1
            word2_idx +=1
        
        word += word1[word1_idx:]
        word += word2[word2_idx:]
        return word