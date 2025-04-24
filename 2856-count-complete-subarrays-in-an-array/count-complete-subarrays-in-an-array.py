class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        distinct_count = len(set(nums))
   
        # O(N)
        res, l, d = 0, 0, {}
        for r, num in enumerate(nums):
            d[num] = d.get(num, 0) + 1

            while len(d) == distinct_count:
                res += N - r
                l_num = nums[l]
                d[l_num] -= 1
                if d[l_num] == 0:
                    del d[l_num]
                l += 1
       
        return res