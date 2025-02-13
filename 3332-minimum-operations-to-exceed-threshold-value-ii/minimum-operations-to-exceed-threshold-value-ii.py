class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # O(N)
        count = 0
        while len(nums) >= 2:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            if x >= k:
                break
            heapq.heappush(nums, x * 2 + y if x < y else y * 2 + x)
            count += 1
        return count
        