# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))

        dummy = ListNode()
        current = dummy
        while heap:
            val, index = heappop(heap)
            current.next = lists[index]
            current = current.next
            lists[index] = lists[index].next
            if lists[index]:
                heappush(heap, (lists[index].val, index))
        return dummy.next      