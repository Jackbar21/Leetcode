# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res
        while list1 and list2:
            if list1.val < list2.val:
                # res.next = ListNode(list1.val)
                res.next = list1
                list1 = list1.next
            else:
                # res.next = ListNode(list2.val)
                res.next = list2
                list2 = list2.next
            res = res.next
        
        # while list1:
        #     res.next = ListNode(list1.val)
        #     res = res.next
        #     list1 = list1.next
        
        # while list2:
        #     res.next = ListNode(list2.val)
        #     res = res.next
        #     list1 = list2.next

        res.next = list2 if not list1 else list1
        return head.next
        