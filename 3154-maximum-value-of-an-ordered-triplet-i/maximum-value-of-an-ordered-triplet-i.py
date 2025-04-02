class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # return max(0, max(((nums[i] - nums[j]) * nums[k]) for i in range(len(nums)) for j in range(i + 1, len(nums)) for k in range(j + 1, len(nums))))
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(N):
                if not (i < j): continue
                for k in range(N):
                    if not (j < k): continue
                    val = (nums[i] - nums[j]) * nums[k]
                    res = max(res, val)
        return res
                    