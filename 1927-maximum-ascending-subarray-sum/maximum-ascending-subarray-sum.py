class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = 0
        res = 0
        prev_num = float("-inf")
        for num in nums:
            if prev_num < num:
                cur_sum += num
                prev_num = num
                continue
            
            res = max(res, cur_sum)
            cur_sum = num
            prev_num = num
        
        return max(res, cur_sum)