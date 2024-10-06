class Solution:
    def __init__(self):
        self.memo = {}
        self.cost = None
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        return self.minCostClimbingStairsDp(len(cost))
    
    def minCostClimbingStairsDp(self, i):
        if i in self.memo:
            return self.memo[i]

        if i <= 1:
            return 0
        
        # Case 1: Reach index i by climbing one step
        case1 = self.minCostClimbingStairsDp(i - 1) + self.cost[i - 1]

        # Case 2: Reach index i by climbing two steps
        case2 = self.minCostClimbingStairsDp(i - 2) + self.cost[i - 2]

        # Return the case with cheaper cost
        self.memo[i] = min(case1, case2)
        return self.memo[i]
