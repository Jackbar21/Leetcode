class Solution:
    def trap(self, height: List[int]) -> int:
        # return self.trapSuffixHeights(height)

        N = len(height)

        l, r = 1, N - 2
        prefix_max = height[0]
        suffix_max = height[N - 1]
        res = 0
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
            
            assert suffix_max <= prefix_max
            h = height[r]
            water = suffix_max - h
            if water > 0:
                res += water
            
            r -= 1
            if suffix_max < h:
                suffix_max = h
            continue
        
        return res



    def trapSuffixHeights(self, height: List[int]) -> int:
        N = len(height)
        suffix_max = []
        suffix_height = 0
        for i in range(N - 1, -1, -1):
            suffix_height = max(suffix_height, height[i])
            suffix_max.append(suffix_height)
        suffix_max = suffix_max[::-1]
        suffix_max.append(0)

        res = 0
        prefix_height = 0
        for i, h in enumerate(height):
            bottleneck_height = suffix_max[i + 1]
            if prefix_height < bottleneck_height:
                bottleneck_height = prefix_height

            if bottleneck_height > h:
                res += bottleneck_height - h
            
            if prefix_height < h:
                prefix_height = h

        return res