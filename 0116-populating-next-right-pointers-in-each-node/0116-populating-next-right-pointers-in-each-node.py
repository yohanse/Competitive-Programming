"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
            
        curr = root
        while curr.left:
            left_child = curr.left
            curr.left.next = curr.right
            previous = curr
            curr_next = curr.next
            while curr_next:
                curr_next.left.next = curr_next.right
                previous.right.next = curr_next.left
                previous = curr_next
                curr_next = curr_next.next
            curr = left_child
        return root

        