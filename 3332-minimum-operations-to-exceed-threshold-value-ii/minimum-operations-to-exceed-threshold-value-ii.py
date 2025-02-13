class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) >= 2 and nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            new_val = x * 2 + y if x < y else y * 2 + x
            heapq.heappush(nums, new_val)
            count += 1
        return count
        