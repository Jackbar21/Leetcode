# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.nums_set = None
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if self.nums_set is None:
            self.nums_set = set(nums)

        if not head:
            return None
        
        # if head.val in self.nums_set:
        rest = self.modifiedList(nums, head.next)
        if head.val in self.nums_set:
            return rest
        
        head.next = rest
        return head
        
