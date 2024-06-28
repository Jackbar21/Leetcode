# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            nxt = head.next
            while nxt and nxt.val == head.val:
                nxt = nxt.next
            head.next = nxt
            head = nxt
        return res