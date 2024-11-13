class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0

        i, j = 0, len(nums) - 1
        while i < j:
            num = nums[i] + nums[j]
            # Number too small, so increase left pointer
            if lower > num:
                i += 1
                # continue
            
            
            # Number too large, so decrease right pointer
            elif num > upper:
                j -= 1
                # continue
            else:

                # At this point, we can either choose: 
                #   (1) count number of fair pairs (i, k), i < k <= j, then increment i
                #   (2) count number of fair pairs (k, j), i <= k < j, then decrement j
                # The point is to commit to one, and then use BINARY SEARCH to find
                # pivot that makes k true (to then count # fair pairs in O(1) time.)

                # I will choose to make index i fixed, and index j variable (i.e. option (1))
                # Since index j is variable, we can ONLY make our number SMALLER. Therefore,
                # for any index k we pick such that i < k <= j, it will always be the case
                # that nums[i] + nums[k] <= nums[i] + nums[j] <= upper. The ONLY thing that can
                # change, is that we make nums[i] + nums[k] SO SMALL that it is NO LONGER >= lower.
                # Hence, find SMALLEST index k, such that i < k <= j, lower <= nums[i] + nums[k].
                # We can do this via leftmost binary search, for which then we know number of
                # valid pairs will be len([(i,k), (i,k+1), (i,k+2), ..., (i,j)]) == j - k + 1.
                l, r = i + 1, j
                k = j
                bound = lower - nums[i]
                while l <= r:
                    mid = (l + r) // 2
                    if bound <= nums[mid]:
                        k = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                # Number of valid pairs 
                # == (j - i + 1) - ((k - 1) - i + 1)
                # == j - i + 1 - (k - 1 - i + 1)
                # == j - i + 1 - (k - i)
                # == j - i + 1 - k + i
                # == j + 1 - k
                # == j - k + 1
                count += j - k + 1

                # Now that we have counted number of valid pairs that start with index i,
                # we can increment it and move forward with the problem.
                i += 1

        return count
