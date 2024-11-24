# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = {}
        index = 0

        cur = head
        while cur:
            d[index] = cur
            index += 1

            # Loop Invariant
            cur = cur.next

        if index == n:
            return head.next

        node = d[index - 1 - n]
        node.next = d.get(index + 1 - n, None)

        return head