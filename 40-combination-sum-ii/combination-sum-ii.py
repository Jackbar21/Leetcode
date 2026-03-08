class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.cache = []
        self.res = set()
        # return list(set([tuple(sorted(arr)) for arr in (self.backtrack(0, 0))]))
        self.backtrack(0, 0)
        return list(self.res)

    def backtrack(self, i, total):
        candidates, target, cache = self.candidates, self.target, self.cache
        N = len(candidates)
        # total = sum(res)

        if total == target:
            self.res.add(tuple(self.cache))
            return

        if i >= N or total > target:
            return        

        num = candidates[i]
        self.cache.append(num)
        self.backtrack(i + 1, total + num)
        self.cache.pop()
        while i + 1 < N and candidates[i] == candidates[i + 1]:
            i += 1
        self.backtrack(i + 1, total)
        return
