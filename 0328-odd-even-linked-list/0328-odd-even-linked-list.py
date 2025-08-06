# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        curr = head
        odd_dummy = ListNode()
        even_dummy = ListNode()
        even_head = even_dummy
        result = odd_dummy
        index = 1

        while curr:
            if index%2:
                odd_dummy.next = curr
                odd_dummy = odd_dummy.next
            else:
                even_dummy.next = curr
                even_dummy = even_dummy.next
            
            index += 1
            curr = curr.next
        
        odd_dummy.next = even_head.next
        even_dummy.next = None

        return result.next
        