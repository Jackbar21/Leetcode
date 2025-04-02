class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # return max(0, max(((nums[i] - nums[j]) * nums[k]) for i in range(len(nums)) for j in range(i + 1, len(nums)) for k in range(j + 1, len(nums))))
        # N = len(nums)
        # res = 0
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         for k in range(j + 1, N):
        #             val = (nums[i] - nums[j]) * nums[k]
        #             if res < val:
        #                 res = val
        # return res
        N = len(nums)

        prefix_max = []
        cur_max = float("-inf")
        for num in reversed(nums):
            if cur_max < num:
                cur_max = num
            prefix_max.append(cur_max)
        prefix_max = prefix_max[::-1]
        
        prefix_min = []
        cur_min = float("inf")
        for num in reversed(nums):
            if cur_min > num:
                cur_min = num
            prefix_min.append(cur_min)
        prefix_min = prefix_min[::-1]
        
        res = 0
        for i in range(N - 2):
            for j in range(i, N - 1):
                # Now, instead of adding a THIRD loop for k, we know that we are MULTIPLYING
                # (nums[i] - nums[j]) BY nums[k]! If nums[i] - nums[j] > 0, then we want
                # index k such that nums[k] == max(nums[j+1:]). If nums[i] - nums[j] < 0, then
                # we want index k such that nums[k] == min(nums[j+1:]) in off-chance smallest
                # value happens to be negative. If nums[i] - nums[j] == 0, then result is 0
                # no matter what.
                # Hence, we can leverage both prefix_min and prefix_max to find potential candidates
                # for highest-value (i, j, k) triplets!

                diff = nums[i] - nums[j]
                case1 = diff * prefix_max[j + 1]
                # case2 = diff * prefix_min[j + 1]
                res = max(res, case1, case1)
        
        return res
