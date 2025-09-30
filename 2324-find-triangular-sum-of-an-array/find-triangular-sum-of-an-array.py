class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        new_nums = []
        for i in range(0, len(nums) - 1):
            new_nums.append((nums[i] + nums[i+1]) % 10)
        return self.triangularSum(new_nums)