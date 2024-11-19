class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Step 1: Populate prefix sums [in O(n) time] to later on be 
        # able to efficiently query the sum of any subarray in O(1) time!
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])
        self.prefix_sums = prefix_sums

        # Initialize hash-map to store elements & frequency of first k values in nums
        d = defaultdict(int)
        for i in range(k):
            num = nums[i]
            d[num] += 1

        l, r = 0, k - 1
        res = 0
        while True:
            # Since using a hash-map to store current values in sliding window of length
            # k at all times, can simply check the total number of distinct keys to
            # verify the current number of distinct elements inside each subarray of length k :)
            if len(d) == k:
                # Get the sum of nums[l..r] in O(1) time
                subarray_sum = prefix_sums[r] - (self.prefix_sums[l - 1] if l > 0 else 0)
                res = max(res, subarray_sum)
            
            # Loop Invariant

            ## (1) Handle left pointer
            if d[nums[l]] > 1:
                d[nums[l]] -= 1
            else:
                # No more occurences of this element in current window!
                del d[nums[l]]
            l += 1

            ## (2) Handle right pointer
            r += 1
            if r >= len(nums):
                # Termination condition!
                break 
            d[nums[r]] += 1
        
        return res
