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

        # Increment res by 2, since every solution starts with a valid (x, y) pair!
        res += 2
        return res if res >= 3 else 0
