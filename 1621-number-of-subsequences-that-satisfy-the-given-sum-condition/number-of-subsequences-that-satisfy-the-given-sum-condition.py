class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        nums.sort()

        res = 0
        for i, min_num in enumerate(nums):
            # Since we're starting at index i, and nums is sorted,
            # 'min_num' will be smallest number. Thus, we want min_num + max_num <= target,
            # for any subsequence such that max_num is largest number in that subsequence.
            # This directly implies that max_num <= target - num. We can binary search
            # to find the rightmost index j such that nums[j] <= target - min_num, where i <= j.
            upper_limit = target - min_num
            if min_num > upper_limit:
                # No more solutions possible
                break

            l, r = i, N - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= upper_limit:
                    # Valid num, look for even better (rightmost) ones!
                    l = mid + 1
                else:
                    # Invalid num, look for smaller but potentially valid ones!
                    r = mid - 1
            
            # Here, we have any subsequence in nums[i..r] is valid where we pick index i
            # Hence, nums[i+1..r] is the range of numbers for which we can either keep
            # or discard each element, for a total of 2 ^ (rightmost - (i + 1) + 1) total
            # combinations.
            res = (res + pow(2, r - i, MOD)) % MOD
        
        return res
