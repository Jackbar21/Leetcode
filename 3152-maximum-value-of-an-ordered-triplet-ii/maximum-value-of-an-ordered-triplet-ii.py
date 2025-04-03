class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)

        prefix_max = [] # prefix_max[i] == max(nums[i:])
        cur_max = float("-inf")
        for num in reversed(nums):
            if cur_max < num:
                cur_max = num
            prefix_max.append(cur_max)
        prefix_max = prefix_max[::-1]

        suffix_max = [] # suffix_max[i] == max(nums[0..i]) == max(nums[:i+1])
        cur_max = float("-inf")
        for num in nums:
            if cur_max < num:
                cur_max = num
            suffix_max.append(cur_max)
        
        res = 0
        for j in range(1, N - 1):
            best_i = suffix_max[j - 1]
            best_k = prefix_max[j + 1]
            val = (best_i - nums[j]) * best_k
            if res < val:
                res = val

        return res
