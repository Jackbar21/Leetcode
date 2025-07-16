class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N, self.nums, self.memo = len(nums), nums, {}
        return max(1 + self.dp(i, parity, nums[i - 1] % 2) for i in range(1, N) for parity in [0, 1])

    # Time Complexity:
    #   Let N be the length of 'nums'.
    # 
    #   - Number of Subproblems: (N - 1) * 2 * 2 == O(N) 
    #   - Time per Suproblem: O(1)
    #
    # TC: O(N) * O(1) == O(N)
    def dp(self, i: int, parity: int, prev_num_parity: int) -> int:
        if (i, parity, prev_num_parity) in self.memo:
            return self.memo[(i, parity, prev_num_parity)]
        nums = self.nums
        N = len(nums)

        if i >= N:
            return 0
        num = nums[i]

        # Case 1: Include index i (can only do so if parity matches!)
        case1 = float("-inf")
        if (prev_num_parity + num) % 2 == parity:
            case1 = 1 + self.dp(i + 1, parity, num % 2)
        
        # Case 2: Don't include index i
        case2 = self.dp(i + 1, parity, prev_num_parity)

        res = max(case1, case2)
        self.memo[(i, parity, prev_num_parity)] = res
        return res
