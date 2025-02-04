class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = 0
        res = 0
        prev_num = 0
        for num in nums:
            if prev_num < num:
                cur_sum += num
                prev_num = num
                continue
            
            if res < cur_sum:
                res = cur_sum
            cur_sum = num
            prev_num = num
        
        return res if res > cur_sum else cur_sum