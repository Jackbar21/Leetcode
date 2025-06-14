class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        line_sweep = [0] * (N + 1)
        for start, end in queries:
            line_sweep[start] += 1
            line_sweep[end + 1] -= 1
        
        cur_delta = 0
        for i, num in enumerate(nums):
            cur_delta += line_sweep[i]
            if num - cur_delta > 0:
                return False
        return True