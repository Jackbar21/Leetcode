class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        base = 1
        while (perfect_square := base * base) <= n:
            perfect_squares.append(perfect_square)
            base += 1
        self.perfect_squares = perfect_squares
        return self.dp(n)
    
    @cache
    def dp(self, i):
        if i == 0:
            return 0
        
        res = float("inf")
        for perfect_square in self.perfect_squares:
            if perfect_square > i:
                break
            count = 1 + self.dp(i - perfect_square)
            if res > count:
                res = count
        return res