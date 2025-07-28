# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        level = [root]
        result = []
        while level:
            result.append(level[0].val)
            next_level = []
            for node in level:
                if node.right:
                    next_level.append(node.right)
                
                if node.left:
                    next_level.append(node.left)

            level = next_level
            

        return result

        