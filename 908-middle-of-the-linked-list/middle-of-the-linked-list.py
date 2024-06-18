# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        tor, hare = head, head.next
        while hare and hare.next:
            tor = tor.next
            hare = hare.next.next
        
        return tor if not hare else tor.next