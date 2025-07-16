class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        self.nums, self.memo = nums, {}
        # for i in range(N):
        #     for parity in range(2):
        #         print(f"dp({i}, {parity})={self.dp(i, parity)}")
        # return max(max(self.dp(i, 0) for i in range(N)), max(self.dp(i, 1) for i in range(N)))
        res = -1
        for i in range(1, N):
            for parity in [0, 1]:
                length = self.dp(i, parity, nums[i - 1] % 2) + 1
                if res < length:
                    res = length
        return res

    def dp(self, i, parity, prev_num_parity):
        if (i, parity, prev_num_parity) in self.memo:
            return self.memo[(i, parity, prev_num_parity)]
        nums = self.nums
        N = len(nums)

        if i >= N:
            return 0
        num = nums[i]
        
        # Case 1: Include index i
        case1 = -1
        if (prev_num_parity + num) % 2 == parity:
            case1 = 1 + self.dp(i + 1, parity, num % 2)
            # return case1

        # Case 2: Don't include index i
        case2 = self.dp(i + 1, parity, prev_num_parity)

        res = case1 if case1 > case2 else case2
        self.memo[(i, parity, prev_num_parity)] = res
        return res