# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1) # dummy node
        tail = head

        tie_breaker = 0
        # min_heap = [(linked_list.val, linked_list) for linked_list in lists if linked_list]
        min_heap = []
        for linked_list in lists:
            if not linked_list:
                continue
            min_heap.append((linked_list.val, tie_breaker, linked_list))
            tie_breaker -= 1
        heapq.heapify(min_heap) # O(len(lists))
        
        while len(min_heap) > 0:
            val, _, linked_list = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next

            linked_list = linked_list.next
            if linked_list: # Only add back to the heap IF NOT EMPTY!!!
                tie_breaker -= 1
                heapq.heappush(min_heap, (linked_list.val, tie_breaker, linked_list))

        return head.next
