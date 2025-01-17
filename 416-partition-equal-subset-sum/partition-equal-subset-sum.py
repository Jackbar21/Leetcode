class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Idea: to partition nums into two subsets of equal sum, they must each be
        # exactly HALF of the sum of ALL the numbers in nums. Trivially, if the sum is
        # odd, the answer is immediately False as the sum cannot be divided into two in the
        # first place! Otherwise, this problem is essentially Subset Sum, where the target
        # is sum(nums)/2. But this would be a pseudopolynomial time algorithm, so something
        # BETTER we can do is for each index i in nums, ADD it to our current sum if we choose
        # to put it in the FIRST subset, or otherwise SUBTRACT it if we choose to put it in the
        # SECOND subset! That way, if we reach a final sum of 0, we know it's because the sums
        # of the first and second subsets are EQUAL.
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
        res = self.dp(0)[0]
        print(f"{self.memo=}")
        return res
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        if i >= len(self.nums):
            return (False, set())
        
        found_sol, subset_sums = self.dp(i + 1)
        if found_sol:
            self.memo[i] = (True, set())
            return self.memo[i]
        
        num = self.nums[i]
        if num == self.target:
            self.memo[i] = (True, set())
            return self.memo[i]
        new_candidates = set([num])

        for subset_sum in subset_sums:
            new_subset_sum = num + subset_sum
            if new_subset_sum == self.target:
                self.memo[i] = (True, set())
                return self.memo[i]
            
            elif new_subset_sum < self.target:
                new_candidates.add(new_subset_sum)
        
        self.memo[i] = (False, new_candidates.union(subset_sums))
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