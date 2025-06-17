class Solution:
    # def n_choose_k(self, n, k):
    #     return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = pow(10, 9) + 7
        self.n, self.m, self.k = n, m, k
        self.memo = {}

        n_choose_k = lambda n, k: (math.factorial(n) % MOD) / ((math.factorial(k)) * math.factorial(n - k))

        return (math.comb(n - 1, k) * m * pow(m - 1, n - 1 - k, MOD)) % MOD

        return (2 * self.dp(0, 0)) % MOD
    
    def dp_combinatorics(self, i, adj_left):
        if adj_left == 0:
            return 1
        
        if i >= N:
            return int(adj_left == 0)
        


    def dp(self, i, adj_count):
        n, m, k = self.n, self.m, self.k

        if (i, adj_count) in self.memo:
            return self.memo[(i, adj_count)]
        
        if i >= n:
            return int(adj_count == self.k)
        
        # Case 1: Choose same number as previous index (can only do so if i > 0 obviously)
        case1 = self.dp(i + 1, adj_count + 1) if i > 0 else 0

        # Case 2: Choose different number in range [1, m] (can only do so if m > 1)
        case2 = self.dp(i + 1, adj_count) if m > 1 else 0

        res = case1 + case2
        self.memo[(i, adj_count)] = res
        return res