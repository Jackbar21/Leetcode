class Solution:
    def __init__(self):
        self.cuts = []
        self.memo = {}
    def minCost(self, n: int, cuts: List[int]) -> int:
        self.cuts = cuts
        # for i in range(n):
        #     self.memo[(i,i)] = 0
        return self.minCostDp(0, n)

    def minCostDp(self, l, r):
        # if r - l == 1:
        #     return 0

        if (l,r) in self.memo:
            return self.memo[(l,r)]

        self.memo[(l, r)] = float("inf")
        for cut in self.cuts:
            if l < cut < r:
                cur_stick_cost = r - l
                left_stick_cost = self.minCostDp(l, cut)
                right_stick_cost = self.minCostDp(cut, r)
                self.memo[(l, r)] = min(self.memo[(l, r)],
                    cur_stick_cost
                    + left_stick_cost
                    + right_stick_cost
                )
        
        # if no valid cut left, then we are done!
        if self.memo[(l, r)] == float("inf"):
            self.memo[(l, r)] = 0
        
        return self.memo[(l, r)]

        