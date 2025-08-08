class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        return self.dp(n, n)

    @cache
    def dp(self, a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        
        return (
            self.dp(a - 100, b)
            + self.dp(a - 75, b - 25)
            + self.dp(a - 50, b - 50)
            + self.dp(a - 25, b - 75)
        ) / 4