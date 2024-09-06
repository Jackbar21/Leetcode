# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)

        new_head = ListNode(-1) # dummy node
        last_node = new_head

        while head:
            if head.val not in nums_set:
                last_node.next = ListNode(head.val)
                last_node = last_node.next

            # Loop Invariant
            head = head.next
        
        return new_head.next