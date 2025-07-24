# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def postorder(node):
            if not node:
                return 0, 0
            
            l_p, l_max = postorder(node.left)
            r_p, r_max = postorder(node.right)
            return max(l_p, r_p) + 1, max(l_max, r_max, l_p + r_p + 1)
        return postorder(root)[1] - 1
        