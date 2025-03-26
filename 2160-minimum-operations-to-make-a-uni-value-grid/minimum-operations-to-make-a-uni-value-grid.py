class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        M, N = len(grid), len(grid[0])

        # Step 1: Get the median
        nums = sorted(grid[i][j] for i in range(M) for j in range(N))
        L = len(nums)
        # assert L == M * N
        median = nums[L // 2] if L % 2 == 1 else (nums[(L//2) - 1] + nums[L//2]) / 2

        # Step 2: Figure out closest number to median you can turn any number in
        #         grid into (i.e. grid[0][0]) with just +x or -x operations.
        i, j = random.randint(0, M - 1), random.randint(0, N - 1)
        num = nums[0] # smallest num, so need +x operations!
        # assert num <= median
        steps = round((median - num) / x)
        target = num + (steps * x)

        # Step 3: Figure out how many steps to get to target for each num, or return
        #         -1 if not possible for ANY num in grid!
        res = 0
        for num in nums:
            diff = num - target if num > target else target - num
            if diff % x != 0:
                return -1
            res += diff // x
        return res
