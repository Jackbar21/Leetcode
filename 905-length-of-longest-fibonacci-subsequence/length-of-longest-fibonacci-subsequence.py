class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Since arr is STRICTLY increasing, that means every number in arr is UNIQUE.
        # Hence, we can map each number to its index, and use that whenever we "need"
        # a number in one of our DP calls!
        # num_to_index = {}
        # for i, num in enumerate(arr):
        #     num_to_index[num] = i
        # self.num_to_index = num_to_index
        self.nums = set(arr)

        N = len(arr)
        self.memo = {}
        self.arr = arr
        res = 0
        for i, x in enumerate(arr):
            for j in range(i + 1, N):
                y = arr[j]
                length = self.dp(x, y)
                if res < length:
                    res = length

        return res + 2 if res >= 1 else 0

    def dp(self, x, y):
        # if (x, y) in self.memo:
        #     return self.memo[(x, y)]
        # res = 1 + self.dp(y, x + y) if (x + y) in self.nums else 0
        # self.memo[(x, y)] = res
        # return res

        # For some reason, caching as per solution above makes things slower!
        # Hence, just return the raw result :)
        return 1 + self.dp(y, x + y) if (x + y) in self.nums else 0