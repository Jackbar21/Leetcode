class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(N^2) 1D DP solution, which is too slow!
        # self.memo = {}
        # self.nums = nums
        # return self.dp(0)

        # Greedy
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
