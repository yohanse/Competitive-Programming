# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val - 1, head)
        curr = return_ans = dummy
        
        previous = dummy
        while curr:
            if curr.val == val:
                previous.next = curr.next
            else:
                previous = curr
            curr = curr.next

        return return_ans.next
        