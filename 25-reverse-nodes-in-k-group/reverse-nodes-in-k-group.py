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
        while count < k:
            count += 1
            k_node = k_node.next
            if k_node is None:
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

# DOCUMENTATION FOR ABOVE CODE:
# [INPUT] 
#       1 -> 2 -> 3 -> 4 -> 5 
# [STEP 1: Disconnect first k nodes]
#       1 -> 2 | 3 -> 4 -> 5 -- head == 1->2, rest_of_linked_list == 3->4->5
# [STEP 2: Reverse first k nodes]
#       2 -> 1 | 3 -> 4 -> 5 -- head == 1, start_of_linked_list == 2->1, rest_of_linked_list == 3->4->5
# [STEP 3: Apply function recursively]
#       2 -> 1 | 4 -> 3 -> 5 -- head == 1, start == 2->1, rest == reverseKGroup(3->4->5) == 4 -> 3 -> 5
# [STEP 4: Connect linked lists BACK together]
#       2 -> 1 -> 4 -> 3 -> 5 -- start_of_linked_list == 2 -> 1 -> 4 -> 3 -> 5
# [STEP 5: Return start_of_linked_list]
#       2 -> 1 -> 4 -> 3 -> 5