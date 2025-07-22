class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = defaultdict(int)
        l = 0
        res = cur_sum = 0
        for r, num in enumerate(nums):
            d[num] += 1
            cur_sum += num
            if d[num] > 1:
                flag = True
                while flag:
                    l_num = nums[l]
                    d[l_num] -= 1
                    cur_sum -= l_num
                    l += 1
                    flag = l_num != num
            
            if res < cur_sum:
                res = cur_sum
        
        return res
