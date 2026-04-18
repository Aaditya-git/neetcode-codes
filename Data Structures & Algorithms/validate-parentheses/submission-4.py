class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = { '(':')', '[':']', '{':'}' }
        stack = []

        for char in s:
            if char in valid_dict:
                stack.append(char)
            
            else:
                if stack ==[] or valid_dict[stack.pop()]!= char:
                    return False
                
        return True if stack==[] else False