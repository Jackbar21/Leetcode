class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(N^2) 1D DP solution, which is too slow!
        # self.memo = {}
        # self.nums = nums
        # return self.dp(0)

        N = len(nums)
        dp = [False] * N
        dp[-1] = True
        for i in range(N - 1, -1, -1):
            steps = nums[i]
            lower = i + 1
            upper = steps + i + 1
            if upper > N:
                upper = N
            # found_sol = False
            for reachable_index in range(lower, upper):
                if dp[reachable_index]:
                    dp[i] = True
                    # found_sol = True
                    break
            # if not found_sol:
            #     return False
            # dp[i] = nums[i] - (N - i) >= N - 1
        # print(f"{dp}")
        return dp[0]






        # Greedy (Accepted, Slow)
        """
        N = len(nums)
        i = 0
        while True:
            # From current index, always go to one that can bring you the FARTHEST,
            # as it covers all possible options! I.e. Greedy-stays-ahead!
            steps = nums[i]
            best_index = None
            best_value = float("-inf")
            for reachable_index in range(i + 1, min(steps + i + 1, N)):
                value = (reachable_index - i) + nums[reachable_index]
                if value > best_value:
                    best_value = value
                    best_index = reachable_index
                
            # At the last index, so return True!
            if i == N - 1:
                return True
            
            # Stuck at current index! Since Greedy stays ahead, must be no solution :(
            if best_index is None:
                return False
            
            # Loop Invariant
            i = best_index

        raise Exception("Unreachable Code")
        """

    # Time Complexity:
    #   - O(N) subproblems, where N = len(nums)
    #   - O(N) time / suproblem
    #   == O(N^2) time complexity
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        N = len(self.nums)
        if i >= N - 1:
            return i == N - 1

        steps = self.nums[i]
        res = False
        for reachable_index in range(i + 1, steps + i + 1):
            if self.dp(reachable_index):
                res = True
                break
        self.memo[i] = res
        return res
