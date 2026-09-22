class Solution:
    def minDeletions(self, s: str) -> int:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        values = sorted(d.values())

        used = set()
        res = 0
        for val in values:
            while val > 0 and val in used:
                val -= 1
                res += 1
            if val > 0:
                used.add(val)
        return res
