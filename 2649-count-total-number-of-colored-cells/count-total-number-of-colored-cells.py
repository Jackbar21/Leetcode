class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * (n - 1) * n // 2