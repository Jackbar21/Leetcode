# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKListsHeap(lists)
        # return self.mergeKListsHeapOptimized(lists)
    
    def mergeKListsHeapOptimized(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Instead of using a min_heap of head value, tie breaker, and linked lists, just use 
        # head value, and list INDEX!
        min_heap = [(linked_list.val, index) for index, linked_list in enumerate(lists) if linked_list]
        heapq.heapify(min_heap)

        head = ListNode() # dummy node
        tail = head

        while len(min_heap) > 0:
            val, index = heapq.heappop(min_heap)
            linked_list = lists[index]

            # Step 1: Add node to result list!
            tail.next = ListNode(val)
            tail = tail.next

            # Step 2: Delete head node from linked_list,
            # and only add back to heap if still not empty!
            linked_list = linked_list.next
            lists[index] = linked_list
            if linked_list:
                heapq.heappush(min_heap, (linked_list.val, index))
        
        return head.next
    
    def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1) # dummy node
        tail = head

        tie_breaker = 0
        # min_heap = [(linked_list.val, linked_list) for linked_list in lists if linked_list]
        min_heap = []
        for linked_list in lists:
            if not linked_list:
                continue
            min_heap.append((linked_list.val, tie_breaker, linked_list))
            tie_breaker += 1
        heapq.heapify(min_heap) # O(k)
        
        while len(min_heap) > 1:
            val, _, linked_list = heapq.heappop(min_heap)
            tail.next = ListNode(val)
            tail = tail.next

            linked_list = linked_list.next
            if linked_list: # Only add back to the heap IF NOT EMPTY!!!
                tie_breaker += 1
                heapq.heappush(min_heap, (linked_list.val, tie_breaker, linked_list))
        
        if len(min_heap) == 1:
            _, _, last_linked_list = min_heap.pop()
            tail.next = last_linked_list

        return head.next
