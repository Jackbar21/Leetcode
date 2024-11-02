class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l, res, max_letter = 0, 0, 0

        for r in range(len(s)):
            letter = s[r]
            d[letter] += 1
            max_letter = max(max_letter, d[letter])

            # Length of the window (# letters in total):    r - l + 1
            # Frequency of letter with highest frequency:   max_letter
            # Number of letters we can replace in window:   k
            # Count of non-highest-frequency letters:       (r - l + 1) - max_letter

            # WANT: (r - l + 1) - max_letter <= k
            # Hence, WHILE it is NOT TRUE that (r - l + 1) - max_letter <= k:
            #           keep deleting leftmost-letter
            # <==> while not (r - l + 1) - max_letter <= k
            # <==> while (r - l + 1) - max_letter > k
            # <==> while r - l + 1 - max_letter > k
            # <==> while r - l - max_letter >= k

            while r - l + 1 - max_letter > k:
                d[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
