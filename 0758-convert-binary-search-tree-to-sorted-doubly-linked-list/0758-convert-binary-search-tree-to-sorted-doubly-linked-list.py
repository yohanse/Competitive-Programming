"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        dummy = Node(0)
        head = dummy
        curr, stack = root, []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            temp = curr.right
            dummy.right = curr
            curr.left = dummy
            dummy = dummy.right
            curr = temp
        
        dummy.right = head.right
        head.right.left = dummy

        return head.right
            
        