class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = pow(10, 9) + 7
        SEAT, PLANT = "S", "P"
        self.corridor = corridor
        self.MOD = MOD

        if corridor.count(SEAT) % 2 == 1:
            return 0

        # Create an array that returns next SEAT index
        N = len(corridor)
        next_seat_index = [None] * N
        index = None
        for i in range(N - 1, -1, -1):
            next_seat_index[i] = index
            if corridor[i] == SEAT:
                index = i
        self.next_seat_index = next_seat_index

        self.memo, self.suffix_memo = {}, {}
        return self.dp(0) % MOD

    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        SEAT, PLANT = "S", "P"
        corridor = self.corridor
        N = len(corridor)

        if i >= N:
            return 0
        
        # Currently at index i. Let's find first index j such that corridor[i..j] contains exactly
        # two seats
        j = self.next_seat_index[i]
        if j is None:
            return 0
        if corridor[i] != SEAT:
            j = self.next_seat_index[j]
            if j is None:
                return 0

        # j = i
        # num_seats = 0
        # while j < N and num_seats < 2:
        #     num_seats += corridor[j] == SEAT
        #     j += 1
        # j -= 1
        
        # if num_seats < 2:
        #     return 0
        
        # Find first index k > j such that corridor[k] == SEAT
        # k = j + 1
        # while k < N and corridor[k] != SEAT:
        #     k += 1
        # if k >= N:
        #     return 1 # Include everything (no seat found)
        k = self.next_seat_index[j]
        if k is None:
            return 1 # Include everything (no seat found)
        
        # Earliest barrier we can place is right after index j
        # Latest barrier we can place is right before index k
        res = 0
        # for index in range(j + 1, k + 1):
        #     res += self.dp(index)
        res = self.dp_subarray(j + 1, k) % self.MOD
        self.memo[i] = res
        return res
    
    def dp_suffix(self, i):
        # Returns dp[i] + dp[i + 1] + ...
        if i in self.suffix_memo:
            return self.suffix_memo[i]

        N = len(self.corridor)
        if i >= N:
            return self.dp(i)

        res = self.dp(i) + self.dp_suffix(i + 1)
        self.suffix_memo[i] = res
        return res
    
    def dp_subarray(self, i, j):
        # dp[i..j] = dp[i..N] - dp[j + 1..n]
        return self.dp_suffix(i) - self.dp_suffix(j + 1)