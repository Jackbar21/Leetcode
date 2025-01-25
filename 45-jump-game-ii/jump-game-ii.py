class Solution:
    def jump(self, nums: List[int]) -> int:
        # self.nums = nums
        # self.memo = {}
        # return self.dp(0)

        LAST_INDEX = len(nums) - 1
        i = 0
        cost = 0
        if nums[0] >= LAST_INDEX:
            return cost if i == LAST_INDEX else cost + 1
        
        while True:
            max_reachable_index = i + nums[i]
            if max_reachable_index >= LAST_INDEX:
                return cost if i == LAST_INDEX else cost + 1
            
            best_index, best_val = i, max_reachable_index
            for reachable_index in range(i + 1, max_reachable_index + 1):
                val = reachable_index + nums[reachable_index]
                if val > best_val:
                    best_index = reachable_index
                    best_val = val
            
            # Problem guarantees there is a solution!
            # assert best_index != i

            # Loop Invariant
            i = best_index
            cost += 1
        
        raise Exception("Unreachable Code")


        # BFS solution, MLE
        """
        LAST_INDEX = len(nums) - 1
        queue = collections.deque([(0, 0)]) # cost, index
        while len(queue) > 0:
            cost, index = queue.popleft()
            max_reachable_index = index + nums[index]
            if max_reachable_index >= LAST_INDEX:
                return cost + 1 if index < LAST_INDEX else cost

            for reachable_index in range(index + 1, max_reachable_index + 1):
                val = reachable_index + nums[reachable_index]
                if val > max_reachable_index:
                    queue.append((cost + 1, reachable_index))
        raise Exception("Unreachable Code")
        """
    

    # Working 1D DP solution, but O(N^2) where N = len(nums)
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        LAST_INDEX = len(self.nums) - 1
        if i >= LAST_INDEX:
            return 0 if i == LAST_INDEX else float("inf")
        
        res = float("inf")
        max_reachable_index = i + self.nums[i]
        for reachable_index in range(i + 1, max_reachable_index + 1):
            val = 1 + self.dp(reachable_index)
            if res > val:
                res = val

        self.memo[i] = res
        return res
