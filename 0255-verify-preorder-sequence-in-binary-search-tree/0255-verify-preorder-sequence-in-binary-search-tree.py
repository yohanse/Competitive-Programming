class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = [preorder[0]]
        min_value = -inf

        for index in range(1, len(preorder)):
            if preorder[index] < min_value:
                return False

            while stack and stack[-1] < preorder[index]:
                min_value = max(min_value, stack.pop())
            
            stack.append(preorder[index])
        
        return True