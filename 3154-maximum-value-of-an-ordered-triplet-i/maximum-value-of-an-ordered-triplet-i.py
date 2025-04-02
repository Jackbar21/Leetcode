class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # return max(0, max(((nums[i] - nums[j]) * nums[k]) for i in range(len(nums)) for j in range(i + 1, len(nums)) for k in range(j + 1, len(nums))))
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    val = (nums[i] - nums[j]) * nums[k]
                    if res < val:
                        res = val
        return res
                    