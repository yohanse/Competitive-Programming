# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder_successor = None
        curr = root
        
        # locate the the the node
        while curr.val != p.val:
            if curr.val > p.val:
                inorder_successor = curr
                curr = curr.left
                
            else:
                curr = curr.right

        # Find the inorder successor
        if curr.right == None:
            return inorder_successor
            
        else:
            curr = curr.right
            while curr.left:
                curr = curr.left
            return curr