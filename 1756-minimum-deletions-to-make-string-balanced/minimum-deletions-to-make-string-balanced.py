class Solution:
    def minimumDeletions(self, s: str) -> int:
        num_b_before, num_a_after = 0,0
        for c in s:
            if c == 'a':
                num_a_after += 1
        min_deletions = (num_a_after - 1) if s[0] == 'a' else num_a_after

        for i in range(len(s)):
            if s[i] == 'b':
                num_b_before += 1
            else:
                num_a_after -= 1

            min_deletions = min(min_deletions, num_b_before + num_a_after)

        return min_deletions