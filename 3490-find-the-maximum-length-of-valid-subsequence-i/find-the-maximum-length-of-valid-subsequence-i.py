class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N, self.nums, self.memo = len(nums), nums, {}
        return max(self.dp(i, parity, nums[i - 1] % 2) for i in range(1, N) for parity in range(2))

    def dp(self, i, parity, prev_num_parity):
        if (i, parity, prev_num_parity) in self.memo:
            return self.memo[(i, parity, prev_num_parity)]
        nums = self.nums
        N = len(nums)

        if i >= N:
            return 1
        num = nums[i]

        res = (
            1 + self.dp(i + 1, parity, num % 2)
            if (prev_num_parity + num) % 2 == parity
            else self.dp(i + 1, parity, prev_num_parity)
        )
        self.memo[(i, parity, prev_num_parity)] = res
        return res