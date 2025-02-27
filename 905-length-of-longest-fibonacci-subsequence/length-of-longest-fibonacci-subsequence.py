class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Since arr is STRICTLY increasing, that means every number in arr is UNIQUE.
        # Hence, just keep a hash set of the numbers in arr to lookup if needed value
        # exists, as its existence will be unique and the array is STRICTLY INCREASING,
        # meaning existence of such a number is guaranteed to occur later in the array,
        # making a valid subsequence order-wise!
        nums = set(arr)
        dp = lambda x, y: 1 + dp(y, x + y) if (x + y) in nums else 0

        N = len(arr)
        res = 0
        for i, x in enumerate(arr):
            for j in range(i + 1, N):
                y = arr[j]
                length = dp(x, y)
                if res < length:
                    res = length

        return res + 2 if res >= 1 else 0

    # def dp(self, x, y):
        # if (x, y) in self.memo:
        #     return self.memo[(x, y)]
        # res = 1 + self.dp(y, x + y) if (x + y) in self.nums else 0
        # self.memo[(x, y)] = res
        # return res
