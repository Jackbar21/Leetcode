# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        digits = []
        while head:
            digits.append(head.val)
            head = head.next
        
        res = 0
        power = 1
        for digit in reversed(digits):
            res += digit * power
            power *= 2
        return res
            