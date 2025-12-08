class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        # Let x be the number of nodes we choose to include in left subtree
        # Then, x can be as small as 0 or as large as n - 1. Then for each x,
        # the number of nodes in right subtree will simply be n - 1 - x.
        return 1 if n <= 1 else sum(self.numTrees(x) * self.numTrees(n - 1 - x) for x in range(n))