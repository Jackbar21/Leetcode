class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        if len(nums) <= 1 or total == 0 or total == len(nums):
            return 0

        queue = collections.deque(nums[:total])
        needed_swaps = total - sum(queue) # Number of zeroes
        res = needed_swaps # Initial value, already computed case 

        for l in range(len(nums)):
            popped = queue.popleft()
            added = nums[(l + total) % len(nums)]
            queue.append(added)

            # Update current needed swaps
            needed_swaps += popped
            needed_swaps -= added

            res = min(res, needed_swaps)
        
        return res