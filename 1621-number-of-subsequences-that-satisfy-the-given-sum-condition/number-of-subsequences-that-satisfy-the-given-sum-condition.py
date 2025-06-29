class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7
        nums.sort()

        # Find rightmost index that can form a subsequence of length 1 from itself at
        # very minimum.
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if num + num <= target:
                # Valid solution, look for potentially even more rightmost ones!
                l = mid + 1
            else:
                # Invalid solution, look for smaller but potentially valid ones on the left!
                r = mid - 1
        max_index = r

        res = 0
        for i in range(max_index + 1):
            # Since we're starting at index i, and nums is sorted,
            # 'min_num' will be smallest number. Thus, we want min_num + max_num <= target,
            # for any subsequence such that max_num is largest number in that subsequence.
            # This directly implies that max_num <= target - num. We can binary search
            # to find the rightmost index j such that nums[j] <= target - min_num, where i <= j.
            min_num = nums[i]
            upper_limit = target - min_num
            if min_num > upper_limit:
                # No more solutions possible
                break

            l, r = i, N - 1
            rightmost = None
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= upper_limit:
                    # Valid num, look for even better (rightmost) ones!
                    rightmost = mid
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
    
    @cache
    def dp(self, i):
        nums, target, MOD = self.nums, self.target, self.MOD
        N = len(nums)

        num = nums[i]
        if i == N - 1:
            return int(num + num <= target)

        # Case 1: Don't choose index i
        case1 = self.dp(i + 1)

        # Case 2: Choose index i 
        case2 = None
        # Since we're starting at index i, and nums is sorted,
        # 'num' will be smallest number. Thus, we want num + max_num <= target,
        # for any subsequence such that max_num is largest num in that subsequence.
        # This directly implies that max_num <= target - num. We can binary search
        # to find the rightmost index j such that nums[j] <= target - num, where i <= j.   
        l, r = i, N - 1
        rightmost = i
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target - num:
                # Valid num, look for even better (rightmost) ones!
                rightmost = mid
                l = mid + 1
            else:
                # Invalid num, look for smaller but potentially valid ones!
                r = mid - 1
        
        assert rightmost is not None or r == i
        assert rightmost >= i
        
        # Here, we have any subsequence in nums[i..rightmost] is valid where we pick index i
        # Hence, nums[i+1..rightmost] is the range of numbers for which we can either keep
        # or discard each element, for a total of 2 ^ (rightmost - (i + 1) + 1) total combinations.
        case2 = pow(2, rightmost - i)

        res = case1 + case2
        return res
