class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed_par = set()

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    removed_par.add(i)
        
        for open_par in stack:
            removed_par.add(open_par)
        
        valid_string = []
        for i in range(len(s)):
            if i not in removed_par:
                valid_string.append(s[i])
        
        return "".join(valid_string)
        