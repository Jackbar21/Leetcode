class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        res = []
        count = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                res.append(num)
        
        i = 0
        while i < len(nums):
            nums[i] = res[i] if i < len(res) else 0
            i += 1
        