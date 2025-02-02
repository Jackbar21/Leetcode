class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prefix_max = []
        suffix_max = []
        prefix_height, suffix_height = 0, 0
        for i in range(N):
            prefix_height = max(prefix_height, height[i])
            prefix_max.append(prefix_height)
    
            suffix_height = max(suffix_height, height[N - 1 - i])
            suffix_max.append(suffix_height)
        suffix_max = suffix_max[::-1]

        res = 0
        for i in range(1, N - 1):
            res += max(0, min(prefix_max[i - 1], suffix_max[i + 1]) - height[i])
        return res