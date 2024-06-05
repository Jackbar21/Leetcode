class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        L = [0] * n
        for i in range(n):
            L[i] = 1
            for j in range(i):
                if nums[j] < nums[i] and L[i] < L[j] + 1:
                    L[i] = L[j] + 1
        return max(L)
