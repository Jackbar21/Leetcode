# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Case 1: Zero nodes left
        if not head:
            return head
        
        # Case 2: One node left
        if not head.next:
            return head

        # Case 3: Two or more nodes left (recursive)
        first, second, rest = head, head.next, head.next.next
        gcd = math.gcd(first.val, second.val)
        node = ListNode(gcd)
        first.next = node
        node.next = second
        second = self.insertGreatestCommonDivisors(second)

        return first


