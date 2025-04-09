class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        # Since every num in nums is larger than or equal to k, and we can only make each
        # number SMALLER, we're gonna turn nums into a MAX-HEAP, and keep popping each
        # copy of the current largest number. Then, we will get the first number (if any)
        # that isn't that largest number, and turn these larger numbers into it!
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        res = 0
        while max_heap and (max_num := max_heap[0]) < -k:
            while max_heap and max_heap[0] == max_num:
                heapq.heappop(max_heap)
            res += 1
            # if not max_heap:
            #     break
        
        return res