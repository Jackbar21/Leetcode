# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_ll(self, head):
        if not head or not head.next:
            return head
        
        prev, cur, nxt = None, head, head.next

        while cur:
            nxt = cur.next
            cur.next = prev

            # Loop invariant
            prev = cur
            cur = nxt
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find length of ll
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        # find middle node, i.e. at half ll length
        mid = ((length + 1) // 2) - 1 # -1 so i can make this node.next = None
        mid_node = head
        for i in range(mid):
            # print(mid_node, mid_node.next)
            # print()
            mid_node = mid_node.next
        
        # this is why we did -1 to mid_node: so we can split
        # ll into two halves that we then merge together
        tmp = mid_node.next
        mid_node.next = None
        mid_node = tmp

        # reverse linked list from mid_node
        l2 = self.reverse_ll(mid_node)
        l1 = head
        res = head
        
        while l2:
            assert l1
            tmp = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = tmp
            l1, l2 = tmp, l2_next
            # l1.next.next = tmp
            # l1 = l1.next.next
            # l2 = l2.next
        
        return head