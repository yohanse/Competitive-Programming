# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def postorder(curr):
            if curr is None:
                return -inf, inf, True, 0
            
            left_max, left_min, is_left_bst, left_res = postorder(curr.left)
            right_max, right_min, is_right_bst, right_res = postorder(curr.right)

            if is_left_bst and is_right_bst and right_min > curr.val > left_max:
                return max(right_max, curr.val), min(left_min, curr.val), True, left_res + right_res + 1
            return -inf, inf, False, max(left_res, right_res)
        return postorder(root)[-1]
        