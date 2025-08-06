# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        index = 1
        curr = head
        previous = None
        first = head
        result = head

        while curr:
            temp = curr.next
            if index%2 == 1 and index != 1:
                previous.next = curr.next
                temp1 = first.next
                first.next = curr
                first.next.next = temp1
                first = first.next


            index += 1
            previous = curr
            curr = temp
        return result