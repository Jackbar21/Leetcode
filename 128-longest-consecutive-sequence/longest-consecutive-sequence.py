class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0

        for num in nums:
            # if not beginning of seq - find it later
            if (num - 1) not in hs:
                length = 1
                while (num + length) in hs:
                    length += 1
                res = max(res, length)
        return res
