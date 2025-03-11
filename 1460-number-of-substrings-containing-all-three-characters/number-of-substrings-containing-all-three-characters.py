class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        a, b, c = 0, 0, 0
        l, res = 0, 0
        for r, letter in enumerate(s):
            if letter == "a":
                a += 1
            elif letter == "b":
                b += 1
            else:
                c += 1

            # Continue if not valid substring!
            if a == 0 or b == 0 or c == 0:
                continue

            while True:
                # s[l..r] is valid, as well as s[l..i] for any r <= i < N
                # So, account for all of these, and shift l pointer by one!
                # r,r+1,r+2,...,N-1 --> (N - 1) - r + 1 == N - r total valid substrings.
                res += N - r
                letter = s[l]
                l += 1

                # Update freq, and break if string no longer valid!
                if letter == "a":
                    a -= 1
                    if a == 0: break
                elif letter == "b":
                    b -= 1
                    if b == 0: break
                else:
                    c -= 1
                    if c == 0: break

        return res
