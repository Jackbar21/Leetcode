class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res, prefix_max, suffix_max = 0, 0, 0
        while l <= r:
            if prefix_max < suffix_max:
                # Left wall is bottleneck. So let's compute water gained at
                # index l, and move left wall!
                h = height[l]
                water = prefix_max - h
                if water > 0:
                    res += water

                l += 1
                if prefix_max < h:
                    prefix_max = h
                continue
            
            # assert suffix_max <= prefix_max
            h = height[r]
            water = suffix_max - h
            if water > 0:
                res += water
            
            r -= 1
            if suffix_max < h:
                suffix_max = h
        
        return res
