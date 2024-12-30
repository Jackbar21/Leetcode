class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = pow(10, 9) + 7
        self.low, self.high = low, high
        self.zero, self.one = zero, one
        self.memo = {}
        return self.dp(0) % MOD
    
    def dp(self, cur_len):
        if cur_len > self.high:
            return 0
        
        if cur_len in self.memo:
            return self.memo[cur_len]
        
        is_valid = self.low <= cur_len
        
        # Case 1: Append '0' zero times
        case1 = self.dp(cur_len + self.zero)

        # Case 2: Append '1' one times
        case2 = self.dp(cur_len + self.one)

        res = is_valid + case1 + case2
        self.memo[cur_len] = res
        return res