# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Follow up asks for recursive & iterative solution, so I've implemented both!

        # Iterative solution
        # return self.reverseListIterative(head)

        # Recursive solution
        return self.reverseListRec(head, None)
    
    def reverseListRec(self, cur, prev) -> Optional[ListNode]:
        if not cur:
            return prev

        next_node = cur.next
        cur.next = prev

        # prev = cur
        # cur = next_node
        # return self.reverseListRec(cur, prev)
        return self.reverseListRec(next_node, cur)

    
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None

        prev = None
        cur = head
        while cur:
            next_node = cur.next
            # HAVE: prev -> cur
            # WANT: prev <- cur
            cur.next = prev

            # Loop Invariant
            prev = cur
            cur = next_node

        return prev

