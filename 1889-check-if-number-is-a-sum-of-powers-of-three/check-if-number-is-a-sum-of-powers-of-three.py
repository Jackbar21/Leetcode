class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # self.memo = {}
        # return self.dp(n, 1)

        solutions = set([0])
        max_expo = math.floor(math.log(n, 3))
        for expo in range(max_expo + 1):
            new_solutions = set()
            val = pow(3, expo)
            for solution in solutions:
                new_solutions.add(solution)
                new_solutions.add(solution + val)
            
            solutions = new_solutions
            if n in solutions:
                break
        
        return n in solutions

    def dp(self, n, expo):
        if (n, expo) in self.memo:
            return self.memo[(n, expo)]

        if n <= 0:
            return n == 0
        
        if expo >= n:
            return expo == n
        
        next_expo = expo * 3
        res = self.dp(n - expo, next_expo)
        if not res:
            res = self.dp(n, next_expo)
        self.memo[(n, expo)] = res
        return res
