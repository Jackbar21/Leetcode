# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums into hash-set to allow for O(1) lookups
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
            if cur.val in nums_set:
                # Delete cur since it is invalid... change
                # From:     prev -> cur -> next_node
                #  To:      prev -> next_node
                prev.next = cur.next
            else:
                # Don't delete cur since it is valid...
                # Just update prev correctly for next iteration :)
                prev = cur

            # Loop Invariant
            cur = cur.next

        return head