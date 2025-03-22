# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        k_node = head
        count = 1 # head is first node!
        while k_node and count < k:
            k_node = k_node.next
            count += k_node is not None
        
        if count < k:
            # Less than k remaining nodes, so return list as is!
            return head
        
        # Disconnect first k nodes from rest of linked list
        rest_of_linked_list = k_node.next
        k_node.next = None

        # Reverse first k nodes in linked list
        start_of_linked_list = self.reverseLinkedList(head)

        # Connect first k nodes in linked list (now reversed!)
        # with rest of linked list, to which we'll apply this
        # same algorithm RECURSIVELY!
        head.next = self.reverseKGroup(rest_of_linked_list, k)

        # Return start of linked list, with all 
        # reverse operations applied as needed!
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
