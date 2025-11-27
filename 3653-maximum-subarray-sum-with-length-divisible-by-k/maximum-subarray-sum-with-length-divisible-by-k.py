class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix.append(cur_sum)
        getSubarraySum = lambda i, j: prefix[j] - (prefix[i - 1] if i > 0 else 0)

        self.nums = nums
        self.k = k
        self.getSubarraySum = getSubarraySum

        return max(self.dp(i) for i in range(len(nums)))

    
    # Largest subarray sum starting from index i
    @cache
    def dp(self, i):
        k = self.k
        nums = self.nums
        N = len(nums)

        if i + k - 1 >= N:
            # Not at least k elements
            return float("-inf")

        k_sum = self.getSubarraySum(i, i + k - 1)

        # Case 1: Stop here
        case1 = k_sum

        # Case 2: Continue onwards
        case2 = k_sum + self.dp(i + k)

        return max(case1, case2)
