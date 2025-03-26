class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #print(f"{x=}")
        M, N = len(grid), len(grid[0])
        first_val = grid[0][0]
        res = float("inf")

        # Step 1: Get the average
        # avg = sum(grid[i][j] for i in range(M) for j in range(N)) / (M * N)
        nums = sorted(grid[i][j] for i in range(M) for j in range(N))
        L = len(nums)
        assert L == M * N
        median = nums[L // 2] if L%2 else (nums[(L//2)-1]+nums[L//2])/2
        avg = median
        #print(f"{avg=}")

        # Step 2: Figure out closest number to average you can turn any number in
        #         grid into (i.e. grid[0][0]) with just +x or -x operations.
        i, j = random.randint(0, M - 1), random.randint(0, N - 1)
        # num = grid[i][j]
        num = min(grid[i][j] for i in range(M) for j in range(N))
        #print(f"{i=}, {j=}, {num=}")
        steps = abs(avg - num) / x
        #print(f"IMPORTANT: {steps=}")
        steps = round(steps)
        target = num + (steps * x) if num < avg else num - (steps * x)
        # #print(f"{steps=}, {target=}")

        res = 0
        for i in range(M):
            for j in range(N):
                num = grid[i][j]
                if abs(num - target) % x != 0:
                    return -1 # Not possible!
                else:
                    #print(f"{res=}, {abs(num - target)=}, {abs(num - target) // x=}")
                    res += abs(num - target) / x
        return round(res)

        # for target in [first_val - x, first_val, first_val + x]:
        #     count = self.solver(grid, x, target)
        #     #print(f"{count=}")
        #     if res > count:
        #         res = count

        # return res if res != float("inf") else -1

    # def solver(self, grid, x, target):
    #     M, N = len(grid), len(grid[0])
    #     res = 0
    #     for i in range(M):
    #         for j in range(N):
    #             val = grid[i][j]
    #             if target == val:
    #                 continue
    #             if target == (val - x) or target == (val + x):
    #                 res += 1
    #                 continue

    #             # Not possible!
    #             return -1
        
    #     return res