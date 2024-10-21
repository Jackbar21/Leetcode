class Solution:
    def __init__(self):
        self.s = None

    def maxUniqueSplit(self, s: str) -> int:
        self.s = s
        return self.maxUniqueSplitDp(set(), 0, 0)
    
    def maxUniqueSplitDp(self, hset, l, r):
        # Base Case:
        if r >= len(self.s):
            # assert r == len(self.s)
            substring = self.s[l : r + 1]

            # Not all unique, so return 0.
            if substring in hset:
                return 0

            # Only consider substring if it is not the empty string.
            return len(hset) + (len(substring) > 0)

        # Case 1: Don't split s at index r
        case1 = self.maxUniqueSplitDp(hset.copy(), l, r + 1)

        # Case 2: Split s at index r
        substring = self.s[l : r + 1]
        if substring in hset:
            # Not unique, so only case1 is valid/plausible solution.
            return case1

        hset_copy = hset.copy()
        hset_copy.add(substring)
        case2 = self.maxUniqueSplitDp(hset_copy, r + 1, r + 1)

        return max(case1, case2)