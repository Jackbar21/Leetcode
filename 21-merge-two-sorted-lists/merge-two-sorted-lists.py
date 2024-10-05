# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def llToList(self, head):
        res = []
        while head:
            res.append(head.val)
        return res
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print('koala')
        # Base Cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            return self.mergeTwoLists(list2, list1)

        # head = list1 if list1.val <= list2.val else list2
        # while list1.val > list2.val:
        head = list1
            

        list1_prev = None
        while list1 and list2:
            if list1.val <= list2.val:
                print('dsa')
                list1_prev = list1
                list1 = list1.next
                continue
            
            assert list1.val > list2.val
            print('kek')
            # print(self.llToList(list1), self.llToList(list2))
            # print(self.llToList(list2))
            list2_node = list2
            print(list2_node)
            list2 = list2.next
            # print(self.llToList(list2))
            list2_node.next = None
            print(list2_node)
            # break
        
            # want to sandwchich list2_node between list1_prev and list1
            list1_prev.next = list2_node
            list2_node.next = list1
            # print(self.llToList(list1), self.llToList(list2))

            # list1_prev, list2_prev = list1, list2
            list1_prev = list2_node

        if not list1:
            list1_prev.next = list2
        # else:
        #     list1.next = list2

        return head


        head = ListNode(-1) # dummy node
        cur = head

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 if not list2 else list2
        return head.next