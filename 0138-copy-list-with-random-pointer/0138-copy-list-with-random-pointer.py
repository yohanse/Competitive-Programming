"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_nodes = {}
        new_nodes = {}
        dummy = Node(-1)
        result = dummy

        curr = head
        index = 0
        while curr:
            old_nodes[curr] = index
            new_nodes[index] = Node(curr.val)
            index += 1
            curr = curr.next


        curr = head
        index = 0
        while curr:
            new_node = new_nodes[index]
            dummy.next = new_node
            if curr.random:
                new_node.random = new_nodes[old_nodes[curr.random]]
                
            index += 1
            dummy = dummy.next
            curr = curr.next
        
        return result.next