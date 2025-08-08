class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        return self.dp_before(n, n) + self.dp_equal(n, n) / 2
    
    @cache
    def dp_equal(self, a, b):
        if a <= 0 or b <= 0:
            return 1 if (a <= 0 and b <= 0) else 0
        
        return (
            self.dp_equal(a - 100, b)
            + self.dp_equal(a - 75, b - 25)
            + self.dp_equal(a - 50, b - 50)
            + self.dp_equal(a - 25, b - 75)
        ) / 4
    
    @cache
    def dp_before(self, a, b):
        if a <= 0:
            return 1 if b > 0 else 0
        
        if b <= 0:
            return 0
        
        return (
            self.dp_before(a - 100, b)
            + self.dp_before(a - 75, b - 25)
            + self.dp_before(a - 50, b - 50)
            + self.dp_before(a - 25, b - 75)
        ) / 4