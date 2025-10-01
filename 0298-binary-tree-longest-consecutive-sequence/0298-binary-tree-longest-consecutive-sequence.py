# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def postorder(curr):
            if not curr:
                return 0, 0, -inf
            
            left_longest, left_longest_include, left_val = postorder(curr.left)
            right_longest, right_longest_include, right_val = postorder(curr.right)

            curr_longest_include = 1
            if curr.val + 1 == left_val:
                curr_longest_include = left_longest_include + 1
            
            if curr.val + 1 == right_val:
                curr_longest_include = max(curr_longest_include, right_longest_include + 1)
            
            return max(left_longest, right_longest, curr_longest_include), curr_longest_include, curr.val
        
        return postorder(root)[0]

        