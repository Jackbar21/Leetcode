# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        tortoise = head
        hare = head.next

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True

        return False
        # seen = set()

        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        
        # return False