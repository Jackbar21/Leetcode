class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # return sum((nums[i] == nums[j] and (i * j) % k == 0) for i in range(len(nums)) for j in range(i + 1, len(nums)))

        N = len(nums)
        res = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, N):
                res += num == nums[j] and (i * j) % k == 0
        return res