# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Add all nodes (in order) to array
        arr = []
        while head:
            arr.append(head)
            head = head.next
        
        # l, r = 0, len(arr) - 1
        # while l < r:
    
            
        
        # Step 2: Add elements to new array in re-ordered fashion
        reordered_arr = []
        # left_next = True
        l, r = 0, len(arr) - 1
        while l <= r:
            # next_node = arr.popleft() if left_next else arr.pop()
            # reordered_arr.append(next_node)
            # left_next = not left_next
            reordered_arr.append(arr[l])
            l += 1
            if l < r:
                reordered_arr.append(arr[r])
                r -= 1

        reordered_arr.append(None)
        for i in range(len(reordered_arr) - 1):
            reordered_arr[i].next = reordered_arr[i + 1]
        
        # return arr[0]
        