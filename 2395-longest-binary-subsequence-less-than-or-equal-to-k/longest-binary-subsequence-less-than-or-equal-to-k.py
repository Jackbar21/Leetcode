class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        self.s, self.k, self.memo = s, k, {}
        return self.dp(0)

    def dp(self, i):
        if i in self.memo:
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
        length = 1
        num = 1
        for index in range(i + 1, N):
            bit = s[index]
            new_num = (num * 2) + int(bit)
            if new_num > k:
                break
            num = new_num
            length += 1
        case2 = length
        
        res = case1 if case1 > case2 else case2
        self.memo[i] = res
        return res
