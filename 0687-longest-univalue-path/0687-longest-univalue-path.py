# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.postorder(root)[-1] - 1

    def postorder(self, node):
        if not node:
            # value, pathlength, best answer so far
            return "a", 0, 0
        
        left_value, left_path_length, left_best_answer = self.postorder(node.left)
        right_value, right_path_length, right_best_answer = self.postorder(node.right)

        ans = 0
        if left_value == right_value == "a" or left_value == right_value == node.val or (left_value =="a" and right_value == node.val) or (right_value == "a" and left_value == node.val):
            return node.val, max(left_path_length, right_path_length) + 1, max(left_best_answer, right_best_answer, left_path_length + right_path_length + 1)
        elif left_value == "a" or left_value == node.val:
            return node.val, left_path_length + 1, max(left_best_answer, right_best_answer, left_path_length + 1)
        elif right_value == "a" or right_value == node.val:
            return node.val, right_path_length + 1, max(left_best_answer, right_best_answer, right_path_length + 1)
        return node.val, 1, max(left_best_answer, right_best_answer, 1)
        