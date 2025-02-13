class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # O(N)
        count = 0
        while len(nums) >= 2 and nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y if x < y else y * 2 + x)
            count += 1
        return count
        