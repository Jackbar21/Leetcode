class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.one, self.seven, self.thirty = costs
        self.days = days
        self.DAYS_LEN = len(days)
        self.memo = {}
        return self.dp(0)
    
    def leftmostBinarySearch(self, i, new_day):
        # Returns leftmost index j such that days[j] > new_day
        days = self.days
        l, r = i + 1, self.DAYS_LEN - 1
        while l <= r:
            mid = (l + r) // 2
            if days[mid] > new_day:
                # Valid solution, look for even more leftmost solutions!
                r = mid - 1
            else:
                l = mid + 1
        
        return l
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        # I can safely assume that I'm currently at the day of days[i] - 1.
        # Now, choosing the one/seven/thirty day pass might allow me to move the index i
        # more than others! For each case, I will recursively compute its cost (memoizing
        # the cost for each index i to turn the complexity from exponential down to polynomial).
        days = self.days
        DAYS_LEN = self.DAYS_LEN
        if i >= len(days):
            return 0

        cur_day = days[i] - 1

        # Case 1: Buy 1-day pass
        case1 = self.one + self.dp(i + 1)

        # Case 2: Buy 7-day pass
        new_day = cur_day + 7 # new_day itself IS covered!
        # Want the leftmost index j such that days[j] > new_day
        new_index = self.leftmostBinarySearch(i, new_day)
        case2 = self.seven + self.dp(new_index)

        # Case 3: Buy 30-day pass
        new_day = cur_day + 30 # new_day itself IS covered!
        # new_index = i + 1
        # while new_index < DAYS_LEN and days[new_index] <= new_day:
        #     new_index += 1
        new_index = self.leftmostBinarySearch(new_index, new_day)
        case3 = self.thirty + self.dp(new_index)

        res = min(case1, case2, case3)
        self.memo[i] = res
        return res