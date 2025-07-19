class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        remainders = [num % k for num in nums]
        res = 0
        for x in range(k):
            # dp[i] == longest valid subsequence ending with remainder x
            dp = [0] * k
            for remainder in remainders:
                length = dp[(x - remainder) % k] + 1
                dp[remainder] = length
                if res < length:
                    res = length
        return res