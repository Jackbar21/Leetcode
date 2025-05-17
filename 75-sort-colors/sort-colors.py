class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE, BLUE = 0, 1, 2

        red, white, blue = 0, 0, 0
        for num in nums:
            if num == RED:
                red += 1
            elif num == WHITE:
                white += 1
            else:
                assert num == BLUE
                blue += 1
        
        for i in range(len(nums)):
            if red > 0:
                nums[i] = RED
                red -= 1
            elif white > 0:
                nums[i] = WHITE
                white -= 1
            else:
                assert blue > 0
                nums[i] = BLUE
                blue -= 1
        
        assert red == white == blue == 0
        return nums