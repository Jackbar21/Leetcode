# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If linked list has <= 1 nodes, return immediately
        if not head or not head.next:
            return head
        
        prev = head     # 18
        cur = head.next # 6
        

        while cur:
            node = ListNode(math.gcd(prev.val, cur.val)) # 6'
            prev.next = node
            node.next = cur

            # Loop invariant
            prev = cur
            cur = cur.next
        
        return head




        # 18 -> 6 -> 10 -> 3
        # 18 -> 6'
        # 6' -> 6
        # 18 -> 6' -> 6 -> 10 -> 3


    def insertGreatestCommonDivisorsRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
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


