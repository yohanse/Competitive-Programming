# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def postorder(root):
            if not root:
                return 0, 0, False
            
            l_ans, l_depth, l_infic = postorder(root.left)
            r_ans, r_depth, r_inifc = postorder(root.right)

            if root.val == start:
                return max(l_depth, r_depth), 0, True
            elif l_infic:
                return max(l_ans, l_depth + r_depth + 1), l_depth + 1, True
            elif r_inifc:
                return max(r_ans, l_depth + r_depth + 1), r_depth + 1, True
            else:
                return 0, max(l_depth, r_depth) + 1, False

        return postorder(root)[0]
        

        

        