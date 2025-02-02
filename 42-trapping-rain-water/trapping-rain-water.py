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
            res += max(0, min(prefix_height, suffix_max[i + 1]) - h)
            prefix_height = max(prefix_height, h)
        return res