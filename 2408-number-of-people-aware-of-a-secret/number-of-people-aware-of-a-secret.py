class Solution:
    def peopleAwareOfSecretAttempt(self, n: int, delay: int, forget: int) -> int:
        # Brute Force
        MOD = pow(10, 9) + 7
        queue = [(delay, forget)]

        for i in range(n - 1):
            # Each person in the queue goes through a day
            new_queue = []

            while queue:
                d, f = queue.pop()
                d -= 1
                f -= 1
                if f == 0:
                    continue
                if d <= 0:
                    new_queue.append((delay, forget))
                new_queue.append((d, f))
        
            queue = new_queue
            
        return len(queue) % MOD
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)   # dp[i] = new people who learn on day i
        dp[1] = 1            # Day 1: 1 person knows the secret
        
        # prefix sum to speed up range contributions
        share = 0  
        for day in range(2, n + 1):
            # People start sharing today = dp[day - delay]
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # People forget today = dp[day - forget]
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            dp[day] = share
        
        # Count people who still remember at day n
        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        return ans
