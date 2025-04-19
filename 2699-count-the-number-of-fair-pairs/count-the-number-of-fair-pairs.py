class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        For each index i, we want to find all indices j such that:
            lower <= nums[i] + nums[j] <= upper
        <==>
            lower - nums[j] <= nums[i], nums[i] <= upper - nums[j]
        
        Now if lower - nums[j] <= nums[i], we know that: 
            - lower - num <= nums[i], for any num >= nums[j].

        Similarly, if nums[i] <= upper - nums[j], we know that:
            - nums[i] <= upper - num, for any num <= nums[j]

        Hence, as long as we sort 'nums', for every index i we can simply
        find smallest index j such that lower - nums[j] <= nums[i], and similarly
        find largest index j' such that nums[i] <= upper - nums[j']
        """
        N = len(nums)
        nums.sort()

        res = 0
        for i, num in enumerate(nums):
            # Find leftmost (i.e. smallest) index j such that lower - nums[j] <= num
            leftmost = None
            l, r = i + 1, N - 1 # Only count indices from i + 1 onwards, to enforce restrictions
            while l <= r:
                j = (l + r) // 2
                if lower - nums[j] <= num:
                    # Valid solution, look for even more leftmost ones!
                    leftmost = j
                    r = j - 1
                else:
                    # Invalid solution, look for worse (but maybe valid) ones on the right!
                    l = j + 1
            if leftmost is None:
                continue
            
            # Find rightmost (i.e. largest) index j such that num <= upper - nums[j]
            rightmost = None
            l, r = i + 1, N - 1 # Only count indices from i + 1 onwards, to enforce restrictions
            while l <= r:
                j = (l + r) // 2
                if num <= upper - nums[j]:
                    # Valid solution, look for even more rightmost ones!
                    rightmost = j
                    l = j + 1
                else:
                    # Invalid solution, look for worse (but potentially valid) ones on the left!
                    r = j - 1
            if rightmost is None:
                continue

            res += rightmost - leftmost + 1
        
        return res
