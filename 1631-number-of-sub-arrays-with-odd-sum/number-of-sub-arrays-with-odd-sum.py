class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = pow(10, 9) + 7

        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            # Returns (NUM_EVEN_SUBARRAYS, NUM_ODD_SUBARRAYS)
            # if i == len(arr) - 1:
            #     return (arr[i] % 2 == 0, arr[i] % 2 == 1)
            if i >= len(arr):
                return (0, 0)
            
            num_even, num_odd = dp(i + 1)
            # if arr[i] % 2 == 0:
            #     # Since we have an even number, just by itself it forms a length 1 even subarray!
            #     return (num_even + 1, num_odd)
            
            # # Since we have an odd number, just by itself it forms a length 1 odd subarray!
            # # Since we have an odd number, adding it to any even subarray will make it odd,
            # # and adding it to any odd subarray will make it even, hence we swap the two values!
            # # But of course, we increase number of odd subarrays by one as well, for the singular
            # # element :)
            # return (num_odd, num_even + 1)
            memo[i] = (num_even + 1, num_odd) if arr[i] % 2 == 0 else (num_odd, num_even + 1)
            return memo[i]

        res = 0
        for i in range(N):
            res += dp(i)[1]
        return res % MOD