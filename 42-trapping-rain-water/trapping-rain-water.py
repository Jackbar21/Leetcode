class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        # prefix_max = []
        suffix_max = []
        prefix_height, suffix_height = 0, 0
        for i in range(N - 1, -1, -1):
            suffix_height = max(suffix_height, height[i])
            suffix_max.append(suffix_height)
        # suffix_max = suffix_max[::-1]

        res = 0
        prefix_height = height[0]
        for i in range(1, N - 1):
            res += max(0, min(prefix_height, suffix_max[N - i - 1]) - height[i])
            prefix_height = max(prefix_height, height[i])
        return res