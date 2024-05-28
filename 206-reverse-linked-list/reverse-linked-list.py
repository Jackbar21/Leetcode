# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Linked list already sorted if 0 or 1 total nodes
        if not head or not head.next:
            return head
        
        prev, cur, nxt = None, head, head.next

        while cur:
            # prev -> cur -> next
            # prev <- cur (<- next ... apply recursively)
            nxt = cur.next
            cur.next = prev

            # Loop invariant
            prev = cur
            cur = nxt
        
        return prev

        