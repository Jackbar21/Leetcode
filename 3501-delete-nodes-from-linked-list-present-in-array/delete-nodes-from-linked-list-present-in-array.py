# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)

        # Keep moving head until it is either None or a VALID number (i.e. not in nums)
        while head and head.val in nums_set:
            head = head.next
        
        # If head is None, no valid nums, hence return None
        if not head:
            return None
        
        prev = head
        assert prev is not None and prev.val not in nums_set # i.e. assert prev is valid node
        cur = head.next

        while cur:
            # Delete cur node if it is invalid (i.e. cur.val is in nums_set)
            next_node = cur.next
            if cur.val in nums_set:
                # Delete cur
                # FROM: prev -> cur -> next_node
                # TO: prev -> next_node
                prev.next = cur.next

                # Loop Invariant
                # prev = next_node
                # cur = next_node.next
                cur = next_node
            else:
                # Loop Invariant
                prev = cur
                cur = cur.next

        return head