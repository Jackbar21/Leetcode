class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = pow(10, 9) + 7

        # Compute prefix sums to be able to obtain sum of
        # ANY subarray in arr in O(1) time
        prefix_sums = []
        cur_sum = 0
        for num in arr:
            cur_sum += num
            prefix_sums.append(cur_sum)

        getSubarraySum = lambda i, j: prefix_sums[j] - (prefix_sums[i - 1] if i > 0 else 0) # O(1)
        isOddSubarray = lambda i, j: getSubarraySum(i, j) & 1 # O(1)
        # return sum(isOddSubarray(i, j) for i in range(N) for j in range(i, N)) # O(N^2)

        self.isOddSubarray = isOddSubarray
        self.arr = arr
        self.memo = {}
        EVEN, ODD = 0, 1
        return sum(self.dp(i)[ODD] for i in range(N)) % MOD

    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        # Returns (NUM_EVEN_SUBARRAYS, NUM_ODD_SUBARRAYS)
        # if i == len(self.arr) - 1:
        #     return (self.arr[i] % 2 == 0, self.arr[i] % 2 == 1)
        if i >= len(self.arr):
            return (0, 0)
        
        num_even, num_odd = self.dp(i + 1)
        # if self.arr[i] % 2 == 0:
        #     # Since we have an even number, just by itself it forms a length 1 even subarray!
        #     return (num_even + 1, num_odd)
        
        # # Since we have an odd number, just by itself it forms a length 1 odd subarray!
        # # Since we have an odd number, adding it to any even subarray will make it odd,
        # # and adding it to any odd subarray will make it even, hence we swap the two values!
        # # But of course, we increase number of odd subarrays by one as well, for the singular
        # # element :)
        # return (num_odd, num_even + 1)
        res = (num_even + 1, num_odd) if self.arr[i] % 2 == 0 else (num_odd, num_even + 1)
        self.memo[i] = res
        return res
        

        
        

