# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        result = dummy

        while l1 and l2:
            tot = carry + l1.val + l2.val
            carry = tot // 10
            l1.val = tot % 10

            dummy.next = l1

            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            tot = carry + l1.val
            carry = tot // 10
            l1.val = tot % 10

            dummy.next = l1

            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            tot = carry + l2.val
            carry = tot // 10
            l2.val = tot % 10

            dummy.next = l2

            dummy = dummy.next
            l2 = l2.next
        
        if carry:
            dummy.next = ListNode(carry)
            dummy = dummy.next
            
        dummy.next = None
        return result.next