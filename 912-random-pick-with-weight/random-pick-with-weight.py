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
        self.w = w
        #print(f"{self.w=}")
        #print(f"{self.prefix=}")
        #print(f"{self.total=}")

        # r = random.randint(0, self.total)
        # #print(f"{r=}, {self.pickIndex()}")

        # [1,3,5]

    def pickIndex(self) -> int:
        rand = random.randint(0, self.total - 1)
        # help(random.randint)
        # #print(f"{r=}")
        # return 0
        leftmost = 0
        l, r = 0, len(self.prefix) - 1
        while l <= r:
            mid = (l + r) // 2
            weight = self.prefix[mid]
            # is_valid = weight < rand
            is_valid = rand < weight
            #print(f"{weight=}, {rand=}, {is_valid=}, {mid=}, {leftmost=}")
            if is_valid:
                # good, look for even leftmost solutions
                leftmost = mid
                # l = mid + 1
                r = mid - 1
            else:
                # r = mid - 1
                l = mid + 1

        assert leftmost is not None
        #print(f"{rand=}, {leftmost=}")
        return leftmost

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()