# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = defaultdict(list)
        def postorder(curr):
            if not curr:
                return 0
            
            left = postorder(curr.left)
            right = postorder(curr.right)
            curr_remove = max(left, right) + 1
            traversal[curr_remove].append(curr.val)

            return curr_remove
        
        max_time = postorder(root)
        return [traversal[time] for time in range(1, max_time + 1)]
        