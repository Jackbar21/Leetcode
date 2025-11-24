class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur_num = 0
        for num in nums:
            cur_num <<= 1
            cur_num |= num
            res.append(cur_num % 5 == 0)
        return res