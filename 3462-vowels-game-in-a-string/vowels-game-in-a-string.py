class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for char in s:
            if char in "aeiou":
                return True
        return False