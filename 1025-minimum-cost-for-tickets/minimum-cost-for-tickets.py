class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.one, self.seven, self.thirty = costs
        self.days = days
        self.memo = {}
        return self.dp(0)
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        # I can safely assume that I'm currently at the day of days[i] - 1.
        # Now, choosing the one/seven/thirty day pass might allow me to move the index i
        # more than others! For each case, I will recursively compute its cost (memoizing
        # the cost for each index i to turn the complexity from exponential down to polynomial).
        days = self.days
        DAYS_LEN = len(days)
        if i >= DAYS_LEN:
            return 0

        cur_day = days[i] - 1

        # Case 1: Buy 1-day pass
        case1 = self.one + self.dp(i + 1)

        # Case 2: Buy 7-day pass
        new_day = cur_day + 7 # new_day itself IS covered!
        # Want the leftmost index j such that days[j] > new_day
        j = i + 1
        while j < DAYS_LEN and days[j] <= new_day:
            j += 1
        case2 = self.seven + self.dp(j)

        # Case 3: Buy 30-day pass
        new_day = cur_day + 30 # new_day itself IS covered!
        while j < DAYS_LEN and days[j] <= new_day:
            j += 1
        case3 = self.thirty + self.dp(j)

        res = min(case1, case2, case3)
        self.memo[i] = res
        return res
