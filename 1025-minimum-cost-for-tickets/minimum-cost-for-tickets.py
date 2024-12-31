class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.one, self.seven, self.thirty = costs
        self.days = days
        self.costs = costs
        return self.dp(0)
    
    @cache
    def dp(self, i):
        # I can safely assume that I'm currently at the day of self.days[i] - 1.
        # Now, choosing the one/seven/thirty day pass might allow me to move the index i
        # more than others! For each case, I will recursively compute its cost (memoizing
        # the cost for each index i to turn the complexity from exponential down to polynomial).
        if i >= len(self.days):
            return 0

        cur_day = self.days[i] - 1

        # Case 1: Buy 1-day pass
        case1 = self.one + self.dp(i + 1)

        # Case 2: Buy 7-day pass
        new_day = cur_day + 7 # new_day itself is NOT covered!
        new_index = i
        while new_index < len(self.days) and self.days[new_index] <= new_day:
            new_index += 1
        case2 = self.seven + self.dp(new_index)

        # Case 3: Buy 30-day pass
        new_day = cur_day + 30 # new_day itself is NOT covered!
        while new_index < len(self.days) and self.days[new_index] <= new_day:
            new_index += 1
        case3 = self.thirty + self.dp(new_index)

        return min(case1, case2, case3)
    
    @cache
    def dpOld(self, days_left):
        if days_left <= 0:
            return 0
        
        # Case 1: Buy 1-day pass
        case1 = self.one + self.dp(days_left - 1)

        # Case 2: Buy 7-day pass
        case2 = self.seven + self.dp(days_left - 7)

        # Case 3: Buy 30-day pass
        case3 = self.thirty + self.dp(days_left - 30)

        return min(case1, case2, case3)