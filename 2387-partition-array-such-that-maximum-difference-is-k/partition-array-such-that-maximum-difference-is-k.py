class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        small_num = nums[0]
        for num in nums:
            if num - small_num <= k:
                continue
            
            # Starting a NEW subarray, with first number being 'num'
            # Hence new 'small_num' value will be 'num', and number of
            # subsequences needed is now 1 more!
            small_num = num
            res += 1
        
        return res

