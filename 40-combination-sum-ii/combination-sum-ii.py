class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.res = collections.deque()
        self.backtrack(0, 0, [], None)
        return list(set(self.res))
    
    def backtrack(self, i: int, cur_sum: int, res: list, prev_num = int | None) -> None:        
        if cur_sum >= self.target or i >= len(self.candidates):
            if cur_sum == self.target:
                self.res.append(tuple(res))
            return

        # Case 1: Include num at index i (CAN ONLY DO THIS ONCE!)
        candidate = self.candidates[i]
        new_sum = cur_sum + candidate
        if new_sum < self.target:
            res.append(candidate)
            self.backtrack(i + 1, cur_sum + candidate, res, candidate)
            res.pop()
        elif new_sum == self.target:
            res.append(candidate)
            self.res.append(tuple(res))
            res.pop()
            return

        # Case 2: Don't include num at index i. If candidate is same as prev_num,
        # then do NOT consider this case, as it is unnecessary repeated work!!!
        if prev_num != candidate:
            self.backtrack(i + 1, cur_sum, res, prev_num)
