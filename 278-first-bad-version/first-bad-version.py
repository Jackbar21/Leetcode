# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # essentially leftmost binary search
        # in an n-sized array of True and Falses, i.e.
        # where the i'th element is isBadVersion(i)

        return self.firstBadAcc(0, n, float("inf"))

    def firstBadAcc(self, l, r, cur_index):
        if l > r:
            return cur_index

        mid = l + (r - l)//2

        if isBadVersion(mid):
            cur_index = mid
            return self.firstBadAcc(l, mid-1, cur_index)
        
        # index mid is not a bad version, meaning no
        # index prior to it can be a bad version, so
        # search right array subhalf instead
        return self.firstBadAcc(mid+1, r, cur_index)
