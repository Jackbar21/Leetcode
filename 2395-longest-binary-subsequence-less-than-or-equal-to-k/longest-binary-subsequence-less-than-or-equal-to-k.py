class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        self.s = s
        self.k = k
        self.memo = {}
        return self.dp(0)
        N = len(s)
        res = 0

        if N == 0:
            return 0

        prefix_zeros = collections.deque()
        zero_count = 0
        for letter in reversed(s):
            zero_count += letter == "0"
            prefix_zeros.appendleft(zero_count)
        prefix_zeros = list(prefix_zeros)

        # Firstly, we can 100% use all the leading zeros of s before the first '1'
        # is encountered. We might as well do this, and pretend the remaining portion
        # of s is the string we must work with (and hence assume s beings with 1 for
        # rest of this problem!)

        index_of_first_one = None
        for i, letter in enumerate(s):
            if letter == "1":
                index_of_first_one = i
                break
        
        if index_of_first_one is None:
            # all of s is "0", so can use entire string!
            return N
        
        res += index_of_first_one # All leading zeros can be used!
        s = s[index_of_first_one:]

        # We're now essentially solving the same problem, where s
        # is now guaranteed to start with a "1"
        # self.s = s
        print(f"{self.dp(0)=}")
    
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
        # This means we must find largest number of bits such that we are still <= k
        # We can do this by binary searching for the rightmost index 'r' such that s[i..r]
        # when converted into decimal is still <= k
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
