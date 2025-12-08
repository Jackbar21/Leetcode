class Solution:
    def countTriples(self, n: int) -> int:
        return 2 * ((perfect_squares := set(base * base for base in range(n + 1))) and sum(a * a + b * b in perfect_squares for a in range(1, n + 1) for b in range(a + 1, n + 1)))