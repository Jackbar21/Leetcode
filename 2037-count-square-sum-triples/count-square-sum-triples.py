class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        perfect_squares = set(base * base for base in range(n + 1))
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c_squared = a * a + b * b
                if c_squared in perfect_squares:
                    res += 2 # (Each solution can have a & b swapped, so two of each)
        return res
