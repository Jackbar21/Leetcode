class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        res = []
        zeroes = []
        for num in nums:
            (zeroes if num == 0 else res).append(num)
        return res + zeroes
