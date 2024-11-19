class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        # Initialize hash-map to store elements & frequency of first k values in nums
        d = defaultdict(int)
        cur_sum = 0
        for i in range(k):
            num = nums[i]
            d[num] += 1
            cur_sum += num

        l, r = 0, k - 1
        while True:
            # Since using a hash-map to store current values in sliding window of length
            # k at all times, can simply check the total number of distinct keys to
            # verify the current number of distinct elements inside each subarray of length k :)
            if len(d) == k:
                res = max(res, cur_sum)
            
            # Loop Invariant
            ## (1) Handle left pointer
            l_num = nums[l]
            if d[l_num] > 1:
                d[l_num] -= 1
            else:
                # No more occurences of this element in current window!
                del d[l_num]
            cur_sum -= l_num
            l += 1

            ## (2) Handle right pointer
            r += 1
            if r >= len(nums):
                # Termination condition!
                break 
            r_num = nums[r]
            d[r_num] += 1
            cur_sum += r_num
        
        return res
