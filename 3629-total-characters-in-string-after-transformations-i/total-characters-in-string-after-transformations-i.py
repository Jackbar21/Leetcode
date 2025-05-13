class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = pow(10, 9) + 7
        res = 0
        for char in s:
            offset_from_a = ord(char) - ord("a")
            res += self.dp(t + offset_from_a)
        return res % MOD
    
    # Return letter after applying k transformations on letter 'a'
    @cache
    def dp(self, t):
        # assert t >= 0

        if t <= 25:
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
        return self.dp(t - 26) + self.dp(t - 25)
