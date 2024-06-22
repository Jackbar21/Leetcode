class Solution:
    def __init__(self):
        self.memo = {}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.minCostPos(cost, 0)
    def minCostPos(self, cost, pos):
        if len(cost) <= 1:
            return 0
        
        # Case 1: start at index 0
        if (pos+1) not in self.memo:
            self.memo[pos+1] = self.minCostPos(cost[1:], pos+1)
        case1 = cost[0] + self.memo[pos+1]

        # Case 2: start at index 1
        if (pos+2) not in self.memo:
            self.memo[pos+2] = self.minCostPos(cost[2:], pos+2)
        case2 = cost[1] + self.memo[pos+2]

        return min(case1, case2)


        
