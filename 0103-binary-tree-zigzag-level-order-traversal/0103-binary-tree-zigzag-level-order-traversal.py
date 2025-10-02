# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []
        curr_level = [root]
        order = True

        while curr_level:
            next_level = []
            curr_level_val = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)

                curr_level_val.append(node.val)
            
            if not order:
                curr_level_val.reverse()
                
            order = not order
            levels.append(curr_level_val)
            curr_level = next_level
        
        return levels