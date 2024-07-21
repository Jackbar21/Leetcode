# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        while cur and cur.val == val:
            cur = cur.next
        head = cur

        while cur:
            nxt = cur.next
            while nxt and nxt.val == val:
                nxt = nxt.next
            
            cur.next = nxt
            cur = cur.next
        
        return head