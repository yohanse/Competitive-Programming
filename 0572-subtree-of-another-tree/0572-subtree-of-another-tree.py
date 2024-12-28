# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def traversal(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            left = traversal(node1.left, node2.left)
            right = traversal(node1.right, node2.right)

            return node1.val == node2.val and left and right
        
        def preorder(node):
            if not node:
                return False
            return preorder(node.right) or preorder(node.left) or traversal(node, subRoot)
        return preorder(root)

             