class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.res = []
        self.backtrack(0, 0, [])
        return self.res

    def backtrack(self, i, cur_sum, cur_sol):
        if i >= len(self.candidates) or cur_sum > self.target:
            return

        if cur_sum == self.target:
            self.res.append(tuple(cur_sol))
            return

        # Case 1: Add the same number (potentially again!)
        candidate = self.candidates[i]
        cur_sol.append(candidate)
        self.backtrack(i, cur_sum + candidate, cur_sol)
        cur_sol.pop()

        # Case 2: Finally choose to go beyond this number (at index i)!
        self.backtrack(i + 1, cur_sum, cur_sol)
