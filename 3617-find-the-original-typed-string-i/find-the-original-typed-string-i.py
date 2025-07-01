class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1 # Original word itself
        prev_letter = None
        for letter in word:
            res += prev_letter == letter
            prev_letter = letter
        return res
