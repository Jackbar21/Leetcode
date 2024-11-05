class Solution:
    def minChanges(self, s: str) -> int:
        # One line solution:
        return sum(int(s[i] != s[i + 1]) for i in range(0, len(s), 2))

        num_changes = 0
        for i in range(0, len(s), 2):
            num_changes += s[i] != s[i + 1]
        return num_changes
