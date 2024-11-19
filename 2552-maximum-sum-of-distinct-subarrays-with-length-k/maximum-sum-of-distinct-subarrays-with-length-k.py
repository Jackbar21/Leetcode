class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize hash-map to store elements & frequency of first k values in nums
        d = defaultdict(int)
        cur_sum = 0
        for i in range(k):
            num = nums[i]
            d[num] += 1
            cur_sum += nums[i]

        l, r = 0, k - 1
        res = 0
        while True:
            # Since using a hash-map to store current values in sliding window of length
            # k at all times, can simply check the total number of distinct keys to
            # verify the current number of distinct elements inside each subarray of length k :)
            if len(d) == k:
                # Get the sum of nums[l..r] in O(1) time
                # subarray_sum = prefix_sums[r] - (prefix_sums[l - 1] if l > 0 else 0)
                # res = max(res, subarray_sum)
                res = max(res, cur_sum)
            
            # Loop Invariant

            ## (1) Handle left pointer
            if d[nums[l]] > 1:
                d[nums[l]] -= 1
            else:
                # No more occurences of this element in current window!
                del d[nums[l]]
            cur_sum -= nums[l]
            l += 1

            ## (2) Handle right pointer
            r += 1
            if r >= len(nums):
                # Termination condition!
                break 
            d[nums[r]] += 1
            cur_sum += nums[r]
        
        return res



#                   l   r             
# nums = [1,5,4,2,9,9,9], k = 3

# d = {9: 3} --> len == 1 < k
# cur_sum = 27
# res = 15