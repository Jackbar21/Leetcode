class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        # Want to find the number of UNIQUE numbers that are larger than k! Since if
        # the only unique numbers we have larger than k are X, Y, Z, then we must:
        # (1) Convert Z into Y
        # (2) Convert Y into X
        # (3) Convert X into k
        # So the number of unique numbers larger than k is the solution to this problem!
        larger_nums = set()
        for num in nums:
            if num > k:
                larger_nums.add(num)
        return len(larger_nums)


        # Since every num in nums is larger than or equal to k, and we can only make each
        # number SMALLER, we're gonna turn nums into a MAX-HEAP, and keep popping each
        # copy of the current largest number. Then, we will get the first number (if any)
        # that isn't that largest number, and turn these larger numbers into it!
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        res = 0
        while max_heap and (max_num := -max_heap[0]) > k:
            while max_heap and -max_heap[0] == max_num:
                heapq.heappop(max_heap)
            res += 1

        return res