class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        self.target = sum_nums // 2

        # Sorting the numbers somehow makes code even faster lol...
        # Probably based on the tests themselves :P
        nums.sort()

        self.nums, self.memo = nums, {}
        # return self.dp2d(0, self.target)
        return self.target in self.dp(0)
    
    # dp(i) == set of ALL possible subset sums in nums[i:] (unless target in there!)
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        nums, target = self.nums, self.target

        if i >= len(nums):
            return set([0])
        
        subset_sums = self.dp(i + 1)
        if target in subset_sums:
            self.memo[i] = subset_sums
            return subset_sums
        
        num = nums[i]
        new_candidates = set([num])

        for subset_sum in subset_sums:
            new_subset_sum = num + subset_sum
            if new_subset_sum <= target:
                new_candidates.add(new_subset_sum)
                
        res = new_candidates.union(subset_sums)
        self.memo[i] = res
        return res


    def dp2d(self, i, target):
        if (i, target) in self.memo:
            return self.memo[(i, target)]
        
        if target <= 0:
            return target == 0
        
        if i >= len(self.nums):
            return False
        
        num = self.nums[i]

        # Case 1: Include num in subset
        case1 = self.dp2d(i + 1, target - num)

        # Case 2: Don't include num in subset
        case2 = self.dp2d(i + 1, target)

        res = case1 or case2
        self.memo[(i, target)] = res
        return res
