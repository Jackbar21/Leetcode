class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        line_sweep = {i: 0 for i in range(N + 1)}
        for start, end in queries:
            line_sweep[start] += 1
            line_sweep[end + 1] -= 1
        
        cur_delta = 0
        for i in range(N):
            cur_delta += line_sweep[i]
            if nums[i] - cur_delta > 0:
                return False
        return True