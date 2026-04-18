class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        first_dict = {}
        second_dict = {}

        for index in range(len(s)):
            if s[index] in first_dict:
                first_dict[s[index]] += 1
            else:
                first_dict[s[index]] = 1 
        
        for index in range(len(t)):
            if t[index] in second_dict:
                second_dict[t[index]] += 1
            else:
                second_dict[t[index]] = 1 

        return True if second_dict==first_dict else False