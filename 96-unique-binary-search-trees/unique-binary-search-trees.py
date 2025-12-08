class Solution:
    def numTrees(self, n: int) -> int:
        return self.dp(n)
    
    @cache
    def dp(self, i):
        if i <= 1:
            return 1
        
        # Let x be the number of nodes we choose to include in left subtree
        # Then, x can be as small as 0 or as large as i - 1. Then, the number
        # of nodes in right subtree will simply be i - 1 - x.
        res = 0
        for x in range(i):
            left, right = x, i - 1 - x
            res += self.dp(left) * self.dp(right)
        return res