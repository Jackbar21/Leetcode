class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = pow(10, 9) + 7
        ORD_A = ord("a")
        self.memo = {}
        res = 0
        for char in s:
            offset_from_a = ord(char) - ORD_A
            res = (res + self.dp(t + offset_from_a)) % MOD
        return res
    
    # Return letter after applying k transformations on letter 'a'
    def dp(self, t):
        # assert t >= 0
        if t in self.memo:
            return self.memo[t]

        if t < 26:
            # It takes at minimum 26 transformations to increase length of
            # string that was originally just 'a'
            return 1
        
        # Otherwise, on the 26'th operation, we will have the string "ab"
        # We can then conclude the length will be dictated from running
        # t - 26 more operations on the first letter a, and t - 26 more
        # operations on the second letter b.
        # One thing to denote is that running k transformations on the
        # letter b is the same thing as running k + 1 transformations
        # on the letter a (since a transforms into b in one step!)
        # Therefore, we can recursively define the resulting length
        # to simply be dp(t - 26) for the 'a' character in "ab", as well
        # as dp(t - 26 + 1) == dp(t - 25) for the 'b' character
        res = self.dp(t - 26) + self.dp(t - 25)
        self.memo[t] = res
        return res
