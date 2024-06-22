class Solution:
    def __init__(self):
        # This leetcode problem showed up on my
        # advanced algorithms final exam during college :)
        self.cuts = None
        self.memo = {}

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cuts = cuts
        return self.minCostDp(0, n)
    
    def minCostDp(self, i, j):
        if (i,j) in self.memo:
            return self.memo[(i,j)]

        self.memo[(i,j)] = float("inf")
        for cut in self.cuts:
            if i < cut < j:
                self.memo[(i,j)] = min(self.memo[(i,j)], 
                    j - i
                    + self.minCostDp(i, cut)
                    + self.minCostDp(cut, j)
                )
        
        # In case no cut ever fit in (i,j) interval,
        # in which case we're already done!
        if self.memo[(i,j)] == float("inf"):
            self.memo[(i,j)] = 0
        
        return self.memo[(i,j)]

        