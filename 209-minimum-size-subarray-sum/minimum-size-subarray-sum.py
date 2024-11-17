class Solution:
    # gets sum of nums[i..j] (i.e. INCLUDING index i AND index j!)
    def getSubarraySum(self, i, j):
        # prefix_sums[i] == sum(nums[0..i])
        # ==> sum(nums[i..j]) == prefix_sums[j] - (prefix_sums[i - 1] if i > 0 else 0)
        # return self.prefix_sums[j] - (prefix_sums[i - 1] if i > 0 else 0)
        assert 0 <= i < len(self.nums)
        assert 0 <= j < len(self.nums)
        if i == 0:
            return self.prefix_sums[j]
        
        return self.prefix_sums[j] - self.prefix_sums[i - 1]

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # l = 0
        # cur_sum = 0
        # res = float("inf")
        # for r in range(len(nums)):
        #     cur_sum += nums[r]
            
        #     while cur_sum >= target:
        #         res = min(res, r - l + 1)
        #         cur_sum -= nums[l]
        #         l += 1
        
        # return res if res != float("inf") else 0
        # O(n)
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])
        self.prefix_sums = prefix_sums
        self.nums, self.target = nums, target
        self.memo = {}

        # Cover the case of just one number already being >= target
        if max(nums) >= target:
            return 1

        res = float("inf")
        for i in range(len(nums)):
            case = self.dp(i)
            if case > 0:
                res = min(res, case)
        
        return res if res != float("inf") else 0

    # Returns length of shortest non-empty subarray of nums, with sum of at least k
    # (or -1 if none exists), *** that ENDS at index i ***
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        nums, target = self.nums, self.target
        prefix_sums = self.prefix_sums

        if i <= 0:
            assert i == 0
            return 1 if nums[i] >= target else 0
            return 0
        
        # Idea: binary search for TIGHTEST index l >= 0 such that sum(nums[l..i]) >= target
        # This will be sorted array of [True,...,True, False,...,False], so want RIGHTMOST True.

        l, r = 0, i
        rightmost_index = l

        # First of all, if sum(nums[0..i]) doesn't work, then no solution will! This is
        # because this yields the largest sum :)
        if self.getSubarraySum(0, i) < target:
            return 0

        # Otherwise, find tightest index that still makes sum >= target!
        rightmost_index = 0
        while l <= r:
            mid = (l + r) // 2
            if self.getSubarraySum(mid, i) >= target:
                # Valid solution, so update res, and check for even
                # tighter valid solutions!!
                rightmost_index = max(rightmost_index, mid)
                l = mid + 1
            else:
                # Invalid solution, i.e. subarray too small, so need to make it
                # larger by making window larger, i.e. by making left-pointer earlier/smaller!
                r = mid - 1
        
        res = i - rightmost_index + 1
        self.memo[i] = res
        return res


