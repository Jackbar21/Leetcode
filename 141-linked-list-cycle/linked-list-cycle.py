# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        
        while hare and hare.next and hare.next.next and hare.next.next.next:
            tortoise = tortoise.next.next.next
            hare = hare.next.next.next.next

            if tortoise == hare:
                return True

        return False