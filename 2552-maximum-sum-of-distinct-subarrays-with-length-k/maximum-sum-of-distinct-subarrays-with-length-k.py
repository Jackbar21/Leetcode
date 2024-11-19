class Solution:
    # Get the sum of nums[i..j] in O(1) time
    def getSubarraySum(self, i, j):
        assert 0 <= i < len(self.nums)
        assert 0 <= j < len(self.nums)
        assert i <= j

        if i == 0:
            return self.prefix_sums[j]
        
        return self.prefix_sums[j] - self.prefix_sums[i - 1]
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Step 1: Populate prefix sums [in O(n) time] to later on be 
        # able to efficiently query the sum of any subarray in O(1) time!
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])
        self.prefix_sums = prefix_sums
        self.nums = nums

        # d = {}
        d = defaultdict(int)

        res = 0

        for i in range(k):
            num = nums[i]
            # d[num] = d.get(num, 0) + 1
            d[num] += 1

        l = 0
        r = k - 1
        # for r in range(k - 1, len(nums)):
        while True:
            # Check if current window is valid, and if so, update
            # result as need be
            all_elements_distinct = len(d) == k
            if all_elements_distinct:
                res = max(res, self.getSubarraySum(l, r))
            
            # Loop Invariant
            d[nums[l]] -= 1
            if d[nums[l]] <= 0:
                assert d[nums[l]] == 0
                del d[nums[l]]
            l += 1

            r += 1
            if r >= len(nums):
                break # Termination condition!
            d[nums[r]] += 1
        
        return res