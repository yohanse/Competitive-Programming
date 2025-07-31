# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def find(node):
            if node.right == node.left == None:
                return node.val, node.val, True, node.val, max(node.val, 0)
            
            left_min, left_max, left_is_bst, left_ans, left_max_ans = inf, -inf, True, 0, 0
            right_min, right_max, right_is_bst, right_ans, right_max_ans = inf, -inf, True, 0, 0

            if node.right:
                right_min, right_max, right_is_bst, right_ans, right_max_ans = find(node.right)

            if node.left:
                left_min, left_max, left_is_bst, left_ans, left_max_ans = find(node.left)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                return min(left_min, right_min, node.val), max(left_max, right_max, node.val), True, right_ans + left_ans + node.val, max(left_max_ans, right_max_ans, right_ans + left_ans + node.val)
            
            else:
                return -inf, -inf, False, -inf, max(left_max_ans, right_max_ans)
        return find(root)[-1]
        