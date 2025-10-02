# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
            
        level = [root]
        right_view_val = []
        while level:
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
            right_view_val.append(level[-1].val)
            level = next_level
        return right_view_val

        