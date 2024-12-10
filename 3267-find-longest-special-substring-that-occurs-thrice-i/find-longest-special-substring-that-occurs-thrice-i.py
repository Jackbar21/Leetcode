class Solution:
    def maximumLength(self, s: str) -> int:
        # Example:  "zzzz"
        # One       4-length
        # Two       3-lenghts
        # Three     2-lenghts
        # Four      1-length
        d = defaultdict(int) # (char, length): count
        cur_letter = s[0]
        l = 0
        for r in range(len(s)):
            if s[r] == cur_letter:
                continue # keep incrementing r!
            
            # Otherwise, the letters no longer match
            # So, s[l..r-1] is of same letter, so we have
            # (r-1)-l-1 == r - l many characters that are the same
            # in a row, leaving us with 1 permutation of length r - l,
            # two permutation of length r - l - 1, three permutation of length
            # r - l - 2, ..., r - l permutations of length 1. So, add these all
            # to a resulting dictionary!
            length = r - l
            count = 1
            while l < r:
                d[(cur_letter, length)] += count

                # Loop Invariant
                length -= 1
                count += 1
                l += 1

            # Update cur_letter to new letter!
            cur_letter = s[r]
        
        # Need to cleanup with one last iteration, in case for loop above exited with last
        # character still being the same as char at position/index l!
        r = len(s)
        length = r - l
        count = 1
        while l < r:
            d[(cur_letter, length)] += count
            # Loop Invariant
            length -= 1
            count += 1
            l += 1
        
        res = -1
        for (_, length), value in d.items():
            if value >= 3 and length > res:
                res = length
        return res
