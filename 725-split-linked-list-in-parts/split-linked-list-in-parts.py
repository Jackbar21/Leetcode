# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        
        num_nodes = length // k
        remainder = length % k

        res = []
        for i in range(k):
            extra_nodes = 1 if i < remainder else 0
            new_ll, head = self.popFirstKNodesFromLinkedList(head, num_nodes + extra_nodes)
            res.append(new_ll)
        
        return res

    def popFirstKNodesFromLinkedList(self, head, k):
        # Returns two element tuple,
        # 1. the new linked list
        # 2. the trimmed (original) linked list
        if k <= 0:
            return (None, head)
        
        cur = head
        prev = None
        for _ in range(k):
            prev = cur
            assert cur is not None
            cur = cur.next
        
        prev.next = None

        # head is now new linked list and trimmed off due to prev.next = None
        # cur is now the rest of the linked list
        return (head, cur)

