# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        digits = []
        while head:
            digits.append(str(head.val))
            head = head.next
        return int("".join(digits), 2)
            