class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        return max(j - i for i in range(len(colors)) for j in range(len(colors)) if colors[i] != colors[j])
