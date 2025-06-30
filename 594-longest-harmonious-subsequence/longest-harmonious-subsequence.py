class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        # For each unique number, treat it as the min number, and figure out longest
        # possible subsequence using that as minimum value
        res = 0
        for min_num in d:
            # Difference between min and max must be EXACTLY 1, not less-than-or-equal to 1.
            # So, at least ONE instance of (num + 1) must exist!
            max_num = min_num + 1
            if max_num not in d:
                continue
            
            count = d[min_num] + d[max_num]
            if res < count:
                res = count
        
        return res
