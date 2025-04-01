class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i >= N:
                return 0
            
            points, brainpower = questions[i]

            # Case 1: Solve question i.
            case1 = points + dp(i + 1 + brainpower)

            # Case 2: Skip question i.
            case2 = dp(i + 1)

            res = max(case1, case2)
            memo[i] = res
            return res
        
        return dp(0)