class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        d = {}
        max_num = max(nums)
        max_freq = 0 # Frequency of max num!
        res = 0
        for r, num in enumerate(nums):
            max_freq += num == max_num

            while max_freq >= k:
                res += N - r
                max_freq -= nums[l] == max_num
                l += 1

        return res
