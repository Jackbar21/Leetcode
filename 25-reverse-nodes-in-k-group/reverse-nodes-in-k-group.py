# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def ll_to_array(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # print(f"{self.ll_to_array(head)=}")
        # reversed_ll = self.reverseLinkedList(head)
        # head.next = ListNode(4)
        # print(f"{self.ll_to_array(head)=}")
        # print(f"{self.ll_to_array(reversed_ll)=}")
        if head is None:
            return None

        k_node = head
        count = 1 # head is first node!
        while k_node and count < k:
            k_node = k_node.next
            count += k_node is not None
        
        print(f"{head=}, {count=}")
        if count < k:
            # Less than k remaining nodes, so return list as is!
            return head
        
        rest_of_linked_list = None
        if k_node:
            rest_of_linked_list = k_node.next
            k_node.next = None

        start_of_linked_list = self.reverseLinkedList(head)
        head.next = self.reverseKGroup(rest_of_linked_list, k)

        return start_of_linked_list
    
    def reverseLinkedList(self, head):
        prev = None
        
        while head:
            next_node = head.next
            head.next = prev

            # Loop Invariant
            prev = head
            head = next_node
        
        return prev

        