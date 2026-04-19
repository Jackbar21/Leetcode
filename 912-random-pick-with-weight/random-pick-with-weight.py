class Solution:
    def __init__(self, w: List[int]):
        # Idea: Let S = sum(w). Then we can pick random number between 0 to S - 1,
        # using random library, and find leftmost index i such that sum(w[0..i]) < to
        # that random number. We can do this in O(logN) per call later using initial
        # prefix sums setup and binary search per call.
        prefix = []
        cur_sum = 0
        for weight in w:
            cur_sum += weight
            prefix.append(cur_sum)
        self.prefix = prefix
        self.total = cur_sum

    def pickIndex(self) -> int:
        rand = random.randint(0, self.total - 1)

        leftmost = 0
        l, r = 0, len(self.prefix) - 1
        while l <= r:
            mid = (l + r) // 2
            if rand < self.prefix[mid]:
                # good, look for even more "leftmost" valid solutions
                r = mid - 1
            else:
                # bad, look for rightmost but potentially valid solutions
                l = mid + 1

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()