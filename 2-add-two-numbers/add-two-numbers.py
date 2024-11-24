# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linkedListToNum(self, head):
        res = 0
        base = 1
        while head:
            res += head.val * base
            base *= 10

            # Loop Invariant
            head = head.next
        
        return res
    
    def numToLinkedList(self, num):
        str_num = str(num)

        # Since we need the number to be backwards in the linked list,
        # we can prepend the next digit to the list (instead of append)
        # to obtain the final backward-digits order that we want :)
        head = None
        for digit in str_num:
            node = ListNode(int(digit))
            node.next = head
            head = node
        
        return head


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = self.linkedListToNum(l1), self.linkedListToNum(l2)
        return self.numToLinkedList(num1 + num2)