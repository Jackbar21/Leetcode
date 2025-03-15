class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2

            # Want to check if can reach a capability of mid
            i = 0
            stolen_homes = 0
            while i < N and stolen_homes < k:
                num = nums[i]
                if num <= mid:
                    # Steal the home!
                    stolen_homes += 1
                    i += 2
                else:
                    # Don't steal the home (as would go OVER capability of 'mid')!
                    i += 1
            
            if stolen_homes == k:
                # Valid solution, look for even BETTER ones on the left-hand side!
                r = mid - 1
            else:
                # Invalid solution, look for potentially VALID ones on right-hand side!
                l = mid + 1

        return r + 1
