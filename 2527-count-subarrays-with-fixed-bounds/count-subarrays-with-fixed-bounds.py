class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        # min_indices = [i for i in range(N) if nums[i] == minK]
        # max_indices = [i for i in range(N) if nums[i] == maxK]

        # print(f"{min_indices=}")
        # print(f"{max_indices=}")

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
                    assert len(invalid_indices) == 0 or invalid_indices[-1] < l <= r
                    res += N - r
                else:
                    last_valid = invalid_indices[leftmost] - 1
                    assert l <= r <= last_valid
                    # res += N - last_valid
                    res += last_valid - r + 1
                

                # res += N - r # Invalid, since can be invalid elements to the right of us...
                l_num = nums[l]
                d[l_num] -= 1
                if d[l_num] == 0:
                    del d[l_num]
                l += 1
        return res

            

        
        # I thought the question was count of subarrays where all the numbers
        # are greater-than-or-equal-to minK and less-than-or-equal-to maxK...
        l = 0
        res = []
        r = 0
        while r < len(nums):
            if (nums[r] < minK or nums[r] > maxK):
                if l <= r - 1:
                    res.append((l, r - 1))
                else:
                    print("ALERT!")
                r += 1
                while r < len(nums) and (nums[r] < minK or nums[r] > maxK):
                    r += 1
                l = r

            r += 1
            
        # for r, num in enumerate(nums):
        #     if num < minK or num > maxK:
        #         if l <= r - 1:
        #             res.append((l, r))
        assert l <= r - 1
        res.append((l, r - 1))

        print(f"{res=}, {l=}, {r=}")
        ans = 0
        for l, r in res:
            count = r - l + 1
            ans += (count * (count + 1)) // 2
        return ans
        # return sum(lambda )