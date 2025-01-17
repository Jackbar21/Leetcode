class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False

        if sum_nums == 0:
            return True # all numbers are 0!

        target = sum_nums // 2
        self.target = target
        # nums.sort(reverse=True)
        self.nums, self.memo = nums, {}
        # self.available_sums = set()
        # return self.dp2d(0, target)
        res = self.dp(0)
        # print(f"{self.memo=}")
        return target in res
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        nums, target = self.nums, self.target

        if i >= len(nums):
            return set()
        
        # SOLVED_SET = set([target])

        subset_sums = self.dp(i + 1)
        if target in subset_sums:
            self.memo[i] = subset_sums
            return subset_sums

        num = nums[i]
        # if num == target:
        #     self.memo[i] = subset_sums
        #     return subset_sums
        new_candidates = set([num])

        for subset_sum in subset_sums:
            new_subset_sum = num + subset_sum
            if new_subset_sum == target: # found sol, no need to continue!
                self.memo[i] = set([target])
                return self.memo[i]
                break
            if new_subset_sum < target:
                new_candidates.add(new_subset_sum)
                
        
        self.memo[i] = new_candidates.union(subset_sums)
        return self.memo[i]


    def dp2d(self, i, target):
        if (i, target) in self.memo:
            return self.memo[(i, target)]
        
        if i >= len(self.nums):
            return target == 0
        
        # Since numbers cannot be negative, we know answer is False
        # immediately if target < 0
        if target < 0:
            return False
        
        num = self.nums[i]

        # Case 1: Include num in subset
        case1 = self.dp2d(i + 1, target - num)

        # Case 2: Don't include num in subset
        case2 = self.dp2d(i + 1, target)

        res = case1 or case2
        self.memo[(i, target)] = res
        return res
