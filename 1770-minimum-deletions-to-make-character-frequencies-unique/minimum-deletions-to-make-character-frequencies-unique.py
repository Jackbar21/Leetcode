class Solution:
    def minDeletions(self, s: str) -> int:
        res, used = 0, set()
        for val in Counter(s).values():
            while val > 0 and val in used:
                val -= 1
                res += 1
            if val > 0:
                used.add(val)
        return res
