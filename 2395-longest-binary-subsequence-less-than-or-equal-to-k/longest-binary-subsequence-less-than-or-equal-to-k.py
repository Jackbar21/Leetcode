class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        self.s, self.k, self.memo = s, k, [-1] * (len(s) + 1)
        return self.dp(0)

    def dp(self, i):
        if self.memo[i] != -1:
            return self.memo[i]
        s, k = self.s, self.k

        N = len(s)
        if i >= N:
            return 0 # length 0 string!
        
        bit = s[i]
        if bit == "0":
            return 1 + self.dp(i + 1) # trailing zero!
        
        # If bit is a 1, we must choose whether or not to include it

        # Case 1: Don't include bit
        case1 = self.dp(i + 1)

        # Case 2: Include bit
        #   This means we must find largest number of bits such that we are still <= k
        #   We can do this by binary searching for the rightmost index 'r' such that s[i..r]
        #   when converted into decimal is still <= k
        l, r = i, N - 1
        while l <= r:
            mid = (l + r) // 2
            num = int(s[i:mid+1], 2)
            if num <= k:
                # Valid solution, look for potentially better ones
                l = mid + 1
            else:
                # Invalid solution, look for smaller (but potentially valid) ones
                r = mid - 1
        # We have found rightmost index 'r' such that s[i..r] is <= k in decimal,
        # hence max number of usable characters is simply r - i + 1!
        case2 = r - i + 1
        
        res = case1 if case1 > case2 else case2
        self.memo[i] = res
        return res
