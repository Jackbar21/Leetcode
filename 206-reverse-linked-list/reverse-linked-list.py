# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Follow up asks for recursive & iterative solution, so I've implemented both!
        # return self.reverseListRec(head)
        return self.reverseListIterative(head)
    
    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return None
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return None
        if not head:
            return None
        
        # a -> b -> c, for any arbitrary nodes a,b,c
        # WANT:
        # a <- b <- c

        # 1 -> 2 -> ... -> 5 -> None
        # None <- 1 <- 2 <- ... <- 5
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            # HAVE: prev -> cur -> next_node
            # WANT: prev <- cur <- next_node
            cur.next = prev

            # Loop Invariant
            prev = cur
            cur = next_node

        return prev

