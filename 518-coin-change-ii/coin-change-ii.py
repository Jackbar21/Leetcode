class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # self.coins, self.amount, self.memo = coins, amount, {}
        # return self.dp(0, 0)

        # Let's try a bottom up approach!
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]
        dp[N][amount] = 1

        for i in range(N - 1, -1, -1):
            coin = coins[i]
            if coin > amount:
                dp[i][amount] = dp[i + 1][amount]
                continue

            for cur_amount in range(amount, amount - coin, -1):
                dp[i][cur_amount] = dp[i + 1][cur_amount]
            for cur_amount in range(amount - coin, -1, -1):
                dp[i][cur_amount] = dp[i][cur_amount + coin] + dp[i + 1][cur_amount]
    
        return dp[0][0]
            




    def dp(self, i, amount):
        if (i, amount) in self.memo:
            return self.memo[(i, amount)]
        
        if i >= len(self.coins):
            return amount == self.amount
        
        coin = self.coins[i]

        # Case 1: Use current coin (can only do so if doesn't bring you negative!)
        case1 = self.dp(i, amount + coin) if amount + coin <= self.amount else 0

        # Case 2: Move on to next coin
        case2 = self.dp(i + 1, amount)

        res = case1 + case2
        self.memo[(i, amount)] = res
        return res
