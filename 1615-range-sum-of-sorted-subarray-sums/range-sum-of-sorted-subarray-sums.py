class Solution:
    def __init__(self):
        self.subarrays = []
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix_sums = []
        magic_modulo_num = (10 ** 9) + 7
        assert n == len(nums)
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            prefix_sums.append(cur_sum)
        # print(prefix_sums)
        # return 0

        d = {}
        subarray_sums = []
        for level in range(1,len(nums)+1):
            # d[level] = self.populateSubarraySums(nums, level)
            subarray_sums += self.populateSubarraySums(nums, level)
        # print(d)
        # return 0

        
        subarray_sums.sort()

        res = 0
        for i in range(left-1,right):
            res += subarray_sums[i]
            res %= magic_modulo_num
        return res
        
        # print(d)
        return 0
    
    def populateSubarraySums(self, nums, level):
        if level > len(nums):
            return
        
        if level == len(nums):
            return [sum(nums)]
        
        # level == 3
        # 0-3
        # 1-4
        # 2-5

        cur_sum = 0
        for i in range(level):
            cur_sum += nums[i] # 0,1,2
        res = [cur_sum]
        for i in range(len(nums) - level + 0):
            cur_sum -= nums[i]
            cur_sum += nums[i + level]
            res.append(cur_sum)
        
        return res
