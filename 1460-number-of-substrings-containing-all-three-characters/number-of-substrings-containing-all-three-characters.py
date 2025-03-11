class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        d = {letter: 0 for letter in "abc"}
        is_valid = lambda: all(freq > 0 for freq in d.values())
        l, res = 0, 0
        for r, letter in enumerate(s):
            d[letter] += 1

            while is_valid():
                # s[l..r] is valid, as well as s[l..i] for any r <= i < N
                # So, account for all of these, and shift l pointer by one!
                # r,r+1,r+2,...,N-1 --> (N - 1) - r + 1 == N - r total valid substrings.
                res += N - r
                d[s[l]] -= 1
                l += 1
            
        while is_valid():
            # s[l..r] is valid, as well as s[l..i] for any r <= i < N
            # So, account for all of these, and shift l pointer by one!
            # r,r+1,r+2,...,N-1 --> (N - 1) - r + 1 == N - r total valid substrings.
            res += N - r
            d[s[l]] -= 1
            l += 1

        return res

            