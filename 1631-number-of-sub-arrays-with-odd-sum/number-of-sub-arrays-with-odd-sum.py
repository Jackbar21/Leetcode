class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Top-Down DP, still O(N)
        # return self.numOfSubarraysTopDown(arr) 

        # Bottom-Up DP, O(1) space
        N = len(arr)
        MOD = pow(10, 9) + 7
        res, num_even, num_odd = 0, 0, 0
        for i in range(N):
            num_even, num_odd = (num_odd, num_even + 1) if arr[i] & 1 else (num_even + 1, num_odd)
            res += num_odd
        return res % MOD
        

    def numOfSubarraysTopDown(self, arr: List[int]) -> int:
        # O(N) algorithm
        N = len(arr)
        MOD = pow(10, 9) + 7

        memo = {}
        def dp(i):
            # Returns (NUM_EVEN_SUBARRAYS, NUM_ODD_SUBARRAYS)
            if i in memo:
                return memo[i]

            # Base Case: End of subarray, empty subarray => no even / odd sum subarrays!
            if i >= len(arr):
                return (0, 0)
            
            # Get number of even & odd subarrays from index i+1 onwards recursively!
            num_even, num_odd = dp(i + 1)

            # If number is odd, then it will form a length 1 odd subarray, and all even subarrays from
            # index i+1 onwards will now become odd subarrays after including number at index i, and
            # similarly all odd subarrays will now become even subarrays!
            if arr[i] & 1:
                memo[i] = (num_odd, num_even + 1)
                return memo[i]
            
            # If number is even, then it will form a length 1 even subarray, and all even subarrays
            # from index i+1 onwards will remain even after including number at index i, and similarly
            # for all odd subarrays!
            memo[i] = (num_even + 1, num_odd)
            return memo[i]

        res = 0
        for i in range(N):
            res += dp(i)[1] # Index 1 is for odd sum counts!
        return res % MOD

# There are K subarrays of odd sum in nums that start at index (i + 1)
# Then if nums[i] is EVEN, then we know there are STILL K subarrays of odd sum from index i onwards!

# O subarrays that are odd sum from index i + 1, and E subarrays of even sum
# If index i is a number that is ODD