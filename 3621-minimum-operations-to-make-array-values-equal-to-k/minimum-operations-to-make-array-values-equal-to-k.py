class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        larger_nums = set()
        for num in nums:
            if num > k:
                larger_nums.add(num)
        return len(larger_nums)
