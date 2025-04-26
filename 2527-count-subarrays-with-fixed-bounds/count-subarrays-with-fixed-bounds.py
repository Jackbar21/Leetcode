class Solution:
    # I will write down my solution in case you cannot hear me on the bus!
    # Essentially, we want to count how many subarrays have minimum value EXACTLY minK
    # and maximum value EXACTLY maxK. So, we can first grab ALL the invalid indices inside
    # of nums, i.e. ones whose value is smalelr than minK or larger than maxK -- as subarrays
    # containing any of those indices are INVALID. 
    #
    # Once that's done, we can do a simple sliding window technique where we use a frequency
    # hash map: a hash map that maps numbers to their current frequencies in the current sliding
    # window. At ANY point, if we come accross an INVALID number (i.e. one at one of those invalid
    # indices), then we must RESTART a NEW sliding window array as the current one would become invalid!
    #
    # Now with that, we know our current window will NEVER contain values SMALLER than minK nor
    # LARGER than maxK. Since we're using a frequency hash map, we can check if there's at least
    # one occurrance of both minK and maxK in our sliding window. If so, then the current window
    # is VALID (i.e. nums[l..r]). We also know that it is valid for any index R, where r <= R,
    # as long as every index in range [r,R] maps to a VALID index in nums! Hence, we can check
    # for the next invalid index after index r using leftmost binary search on our initial
    # 'invalid_indices' array! Then, we can take that index and decrement one from it to correctly
    # find index R (i.e. the last valid index is the one right before the first invalid index after r!)
    # We use that to compute the number of remaining valid windows that start at index l, and then
    # increment index l (with remembering to decrement the frequency of the number at index l by
    # one in our current window frequency hash-map!) 

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        invalid_indices = [i for i in range(N) if (nums[i] < minK or nums[i] > maxK)]

        # Since its now about equal to counts, maybe sliding window is perfect here?
        d = {}
        l = 0
        res = 0
        for r, num in enumerate(nums):
            if num < minK or num > maxK:
                # Invalid, start new window
                l = r + 1
                d = {}
                continue

            d[num] = d.get(num, 0) + 1
            while d.get(minK, 0) > 0 and d.get(maxK, 0) > 0:
                # Can only consider valid subarrays up to LAST valid number!
                # Hence, binary search over invalid indices to find leftmost index 'i'
                # such that r <= i, and then i - 1 is the MAX index we can go up to.
                left, right = 0, len(invalid_indices) - 1
                leftmost = None
                while left <= right:
                    mid = (left + right) // 2
                    if r <= invalid_indices[mid]:
                        # Valid index, look for even tighter ones on the left!
                        leftmost = mid
                        right = mid - 1
                    else:
                        # Invalid index, look to right
                        left = mid + 1
                
                # If leftmost is still None, that means there's no more invalid indices!
                if leftmost is None:
                    # assert len(invalid_indices) == 0 or invalid_indices[-1] < l <= r
                    res += N - r
                else:
                    last_valid = invalid_indices[leftmost] - 1
                    # assert l <= r <= last_valid
                    res += last_valid - r + 1

                # Increment 'l' pointer!
                l_num = nums[l]
                d[l_num] -= 1
                if d[l_num] == 0:
                    del d[l_num]
                l += 1

        return res
