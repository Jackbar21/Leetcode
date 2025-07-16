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
        
        # Case 1: Include index i
        case1 = -1
        if (prev_num_parity + num) % 2 == parity:
            case1 = 1 + self.dp(i + 1, parity, num % 2)
            self.memo[(i, parity, prev_num_parity)] = case1
            return case1
            # return case1

        # Case 2: Don't include index i
        case2 = self.dp(i + 1, parity, prev_num_parity)

        res = case1 if case1 > case2 else case2
        self.memo[(i, parity, prev_num_parity)] = res
        return res