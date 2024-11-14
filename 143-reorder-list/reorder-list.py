# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Add all nodes (in order) to array
        arr = []
        while head:
            arr.append(head)
            tmp_next = head.next
            head.next = None
            head = tmp_next

        # Step 2: Set nodes' next values respective to needed reordering :)
        l, r = 0, len(arr) - 1
        while l < r - 1:
            cur_head = arr[l]
            cur_tail = arr[r]

            cur_head.next = cur_tail
            cur_tail.next = arr[l + 1]

            # Loop Invariant
            l += 1
            r -= 1

        # Handle last case, where end of linked list must be None!
        if l < r:
            cur_head = arr[l]
            cur_tail = arr[r]

            cur_head.next = cur_tail
            cur_tail.next = None

        return