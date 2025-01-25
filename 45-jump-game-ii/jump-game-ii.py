class Solution:
    def jump(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return self.dp(0)
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        LAST_INDEX = len(self.nums) - 1
        if i >= LAST_INDEX:
            return 0 if i == LAST_INDEX else float("inf") # TODO: Maybe float("inf") if > LAST_INDEX ?
        
        res = float("inf")
        max_reachable_index = i + self.nums[i]
        for reachable_index in range(i + 1, max_reachable_index + 1):
            res = min(
                res,
                1 + self.dp(reachable_index)
            )
        
        self.memo[i] = res
        return res

        

