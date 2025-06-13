class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        N = len(nums)
        if p == 0:
            return 0

        nums.sort()

        min_diff = 0
        max_diff = nums[-1] - nums[0]

        l, r = min_diff, max_diff
        while l <= r:
            mid = (l + r) // 2

            # Get number of pairs that have max difference <= mid
            count = 0
            i = 1
            while i < N:
                num = nums[i]
                prev_num = nums[i - 1]
                if abs(num - prev_num) <= mid:
                    count += 1
                    i += 1 # Cannot reuse indices

                # Loop Invariant
                i += 1
            
            if count >= p:
                # Valid solution, look for even better left-most ones
                r = mid - 1
            else:
                # Too small, look for bigger but valid solutions on right
                l = mid + 1
        
        return l
