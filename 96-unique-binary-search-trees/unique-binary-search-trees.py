class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        return 1 if n <= 1 else sum(self.numTrees(x) * self.numTrees(n - 1 - x) for x in range(n))