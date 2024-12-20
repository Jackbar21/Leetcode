class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.res = set()
        self.memo = set()
        self.backtrack(0, 0, [])
        return list(self.res)
    
    def backtrack(self, i: int, cur_sum: int, res: list) -> None:        
        tuple_res = tuple(res)
        if (tuple_res, cur_sum) in self.memo:
            return
        if cur_sum == self.target:
            self.res.add(tuple(sorted(res)))
            return
        
        # No more possible solutions!
        if cur_sum > self.target or i >= len(self.candidates):
            return
        
        # Case 1: Include num at index i (CAN ONLY DO THIS ONCE!)
        candidate = self.candidates[i]
        res.append(candidate)
        self.backtrack(i + 1, cur_sum + candidate, res)
        res.pop()

        # Case 2: Don't include num at index i
        self.backtrack(i + 1, cur_sum, res)

        self.memo.add((tuple_res, cur_sum))