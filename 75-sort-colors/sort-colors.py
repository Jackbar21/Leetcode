class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = [0] * 3
        for num in nums:
            color_count[num] += 1
        
        index = 0
        for i in range(3):
            for _ in range(color_count[i]):
                nums[index] = i
                index += 1
        