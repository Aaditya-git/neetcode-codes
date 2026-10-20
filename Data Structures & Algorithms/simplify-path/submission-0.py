class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        list_of_dir = path.split('/')

        for ch in list_of_dir:
            if ch == '' or ch =='.':
                continue
            elif ch == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
            
        return '/' + '/'.join(stack)
        