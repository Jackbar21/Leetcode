class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        self.nums = nums
        # for i in range(N):
        #     for parity in range(2):
        #         print(f"dp({i}, {parity})={self.dp(i, parity)}")
        # return max(max(self.dp(i, 0) for i in range(N)), max(self.dp(i, 1) for i in range(N)))
        res = -1
        for i in range(1, N):
            for parity in [0, 1]:
                case = self.dp(i, parity, nums[i - 1] % 2)
                if res < case:
                    res = case
        return res

    @cache
    def dp(self, i, parity, prev_num_parity):
        nums = self.nums
        N = len(nums)

        if i >= N:
            return 1
        num = nums[i]
        
        # Case 1: Include index i
        case1 = -1
        if (prev_num_parity + num) % 2 == parity:
            # case1 = 2 if False else 1 + remaining
            # case1 = 1 + max(1, self.dp(i + 1, parity))
            case1 = 1 + self.dp(i + 1, parity, num % 2)

        # Case 2: Don't include index i
        case2 = self.dp(i + 1, parity, prev_num_parity)

        res = max(case1, case2)
        return res