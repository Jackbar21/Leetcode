class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Top Down Solution [TLE]
        # self.n, self.k, self.maxPts, self.memo = n, k, maxPts, [0] * (n + 1)
        # return self.dp(0)

        # Bottom Up Solution [TLE]
        # dp = [0] * k + [1] * (n - k + 1)
        # for points in range(k - 1, -1, -1):
        #     for p in range(points + 1, points + maxPts + 1):
        #         if p > n:
        #             break
        #         dp[points] += dp[p] / maxPts
        # return dp[0]

        # Sliding window trick
        dp = [0] * k + [1] * (n - k + 1)
        window_sum = sum(dp[k:k + maxPts])
        for points in range(k - 1, -1, -1):
            dp[points] = window_sum / maxPts
            window_sum += dp[points] - (dp[points + maxPts] if points + maxPts < len(dp) else 0)
        return dp[0]
                
    
    def dp(self, points):
        if (mem := self.memo[points]) > 0:
            return mem

        if points >= self.k:
            res = 1 if points <= self.n else 0
            self.memo[points] = res
            return res
        
        # return sum(self.dp(points + p) for p in range(1, self.maxPts + 1)) / self.maxPts
        res = 0
        max_pts = points + self.maxPts
        if max_pts > self.n:
            max_pts = self.n
        for p in range(points + 1, max_pts + 1):
            res += self.dp(p)
        res /= self.maxPts
        self.memo[points] = res
        return res
