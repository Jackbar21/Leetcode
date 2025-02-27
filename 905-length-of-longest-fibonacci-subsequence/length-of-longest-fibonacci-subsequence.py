class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Since arr is STRICTLY increasing, that means every number in arr is UNIQUE.
        # Hence, we can map each number to its index, and use that whenever we "need"
        # a number in one of our DP calls!
        num_to_index = {}
        for i, num in enumerate(arr):
            num_to_index[num] = i
        self.num_to_index = num_to_index

        N = len(arr)
        self.memo = {}
        self.arr = arr
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                length = 2 + self.dp(i, j)
                if res < length:
                    res = length

        return res if res >= 3 else 0

    def dp(self, i, j):
        # if (i, j) in self.memo:
        #     return self.memo[(i, j)]

        if j >= len(self.arr):
            return 0        

        res = 0
        base = self.arr[i] + self.arr[j]
        index = self.num_to_index.get(base, -1)
        if index > j:
            res = 1 + self.dp(j, index)

        # self.memo[(i, j)] = res
        return res
