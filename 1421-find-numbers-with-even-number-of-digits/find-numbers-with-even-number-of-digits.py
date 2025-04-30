class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # return sum(len(str(num)) % 2 == 0 for num in nums)
        res = 0
        for num in nums:
            num_digits = 0
            while num > 0:
                num //= 10
                num_digits += 1
            if num_digits % 2 == 0:
                res += 1
        return res