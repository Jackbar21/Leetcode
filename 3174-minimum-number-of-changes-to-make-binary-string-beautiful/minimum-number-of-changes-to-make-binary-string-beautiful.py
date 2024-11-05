class Solution:
    def minChanges(self, s: str) -> int:
        # One line solution:
        # return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))

        count = 0
        for i in range(0, len(s), 2):
            count += s[i] != s[i + 1]
        return count