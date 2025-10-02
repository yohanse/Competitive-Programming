"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        
        prev, curr = head, head.next
        
        while True:
            if prev.val <= insertVal <= curr.val:
                break
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    break
            elif head == curr:
                break
            
            prev, curr = curr, curr.next
        
        prev.next = Node(insertVal, curr)
        return head
        
        