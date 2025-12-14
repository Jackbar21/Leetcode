class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Since colors is only lowercase English letters, there's at most 26 unique colors
        self.colors, self.neededTime, self.memo = colors, neededTime, {}
        return self.dp(0, None)
    
    def dp(self, i, prev_color):
        if (i, prev_color) in self.memo:
            return self.memo[(i, prev_color)]

        colors, neededTime = self.colors, self.neededTime
        N = len(colors)

        if i >= N:
            return 0
        
        color = colors[i]
        time = neededTime[i]
        # Case 1: Delete current color
        case1 = time + self.dp(i + 1, prev_color)

        # Case 2: Keep cur color (only possible if prev_color != color)
        case2 = float("inf") if prev_color == color else self.dp(i + 1, color)

        res = case1 if case1 < case2 else case2
        self.memo[(i, prev_color)] = res
        return res
