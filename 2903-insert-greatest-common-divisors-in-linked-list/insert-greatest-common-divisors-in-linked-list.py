# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If linked list has <= 1 nodes, return immediately
        # if not head or not head.next:
        #     return head
        
        prev = head
        cur = head.next
        while cur:
            node = ListNode(math.gcd(prev.val, cur.val))
            prev.next = node
            node.next = cur

            # Loop invariant
            prev = cur
            cur = cur.next
        
        return head
