class Solution:
    def trap(self, height: List[int]) -> int:
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