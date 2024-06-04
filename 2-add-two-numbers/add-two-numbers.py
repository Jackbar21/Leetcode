# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listToNum(lst):
            num, exponent = 0, 0
            while lst:
                num += lst.val * (pow(10, exponent))
                lst = lst.next
                exponent += 1
            return num
        
        res = str(listToNum(l1) + listToNum(l2))[::-1]
        cur = ListNode(0)
        head = cur
        for digit in res:
            cur.next = ListNode(int(digit))
            cur = cur.next
        
        return head.next
                

