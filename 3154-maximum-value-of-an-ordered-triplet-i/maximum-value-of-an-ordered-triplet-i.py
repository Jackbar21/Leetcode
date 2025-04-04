class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        ### O(N^3) solution (one line!) ###
        """
        return max(0, max(((nums[i] - nums[j]) * nums[k]) for i in range(len(nums)) for j in range(i + 1, len(nums)) for k in range(j + 1, len(nums))))
        """
        
        ### O(N^2) solution ##
        """
        prefix_max = [] # prefix_max[i] == max(nums[i:])
        cur_max = float("-inf")
        for num in reversed(nums):
            if cur_max < num:
                cur_max = num
            prefix_max.append(cur_max)
        prefix_max = prefix_max[::-1]
        
        # prefix_min = []
        # cur_min = float("inf")
        # for num in reversed(nums):
        #     if cur_min > num:
        #         cur_min = num
        #     prefix_min.append(cur_min)
        # prefix_min = prefix_min[::-1]
        
        res = 0
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                # Now, instead of adding a THIRD loop for k, we know that we are MULTIPLYING
                # (nums[i] - nums[j]) BY nums[k]! If nums[i] - nums[j] > 0, then we want
                # index k such that nums[k] == max(nums[j+1:]). If nums[i] - nums[j] < 0, then
                # we want index k such that nums[k] == min(nums[j+1:]) in off-chance smallest
                # value happens to be negative. If nums[i] - nums[j] == 0, then result is 0
                # no matter what.
                # Hence, we can leverage both prefix_min and prefix_max to find potential candidates
                # for highest-value (i, j, k) triplets!

                # EDIT: Since in constraints it states that each num in nums is POSITIVE (i.e. >= 1),
                # it can NEVER be that nums[k] is negative! Hence, we don't even need the prefix_min
                # part!

                # diff = nums[i] - nums[j]
                # case1 = diff * prefix_max[j + 1]
                # case2 = diff * prefix_min[j + 1]
                # res = max(res, case1, case2)
                val = (nums[i] - nums[j]) * prefix_max[j + 1]
                if res < val:
                    res = val

        return res
        """

        ### O(N) solution ###
        prefix_max = [] # prefix_max[i] == max(nums[i:])
        cur_max = float("-inf")
        for num in reversed(nums):
            if cur_max < num:
                cur_max = num
            prefix_max.append(cur_max)
        prefix_max = prefix_max[::-1]

        suffix_max = [] # suffix_max[i] == max(nums[0..i])
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
