# HINT: Binary search for the answer. 
#       How can you check how many pairs have distance <= X?
class Solution:
    def __init__(self):
        self.num_pairs = -1
        self.nums = None # sorted!!
    def countNumPairsGreaterThanX(self, X):
        n, l, count = len(self.nums), 0, 0

        for r in range(n):
            count += l
            while self.nums[r] - self.nums[l] > X:
                count += 1
                l += 1

        return count
    def countNumPairsLessThanOrEqualToX(self, X):
        return self.num_pairs - self.countNumPairsGreaterThanX(X)
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        self.nums = nums
        self.num_pairs = n * (n - 1) // 2

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2

            count = self.countNumPairsLessThanOrEqualToX(mid)

            if count >= k:
                r = mid
            else:
                l = mid + 1
        
        return l