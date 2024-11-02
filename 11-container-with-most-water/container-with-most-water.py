class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        l, r = 0, len(height) - 1
        while l < r:
            height_l, height_r = height[l], height[r]
            cur_water = (r - l) * min(height_l, height_r)
            max_water = max(max_water, cur_water)

            if height_l <= height_r:
                while l < r and height[l] <= height_l:
                    l += 1
            else:
                while l < r and height[r] <= height_r:
                    r -= 1
        
        return max_water
