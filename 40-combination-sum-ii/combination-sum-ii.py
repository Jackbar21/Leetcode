class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.res = set()
        self.memo = set()
        self.backtrack(0, 0, [])
        return list(self.res)
    
    def backtrack(self, i: int, cur_sum: int, res: list, prev_num = None) -> None:        
        # tuple_res = tuple(res)
        # if tuple_res in self.memo:
        #     return

        if cur_sum == self.target:
            self.res.add(tuple((res)))
            return
        
        # No more possible solutions!
        if cur_sum > self.target or i >= len(self.candidates):
            return
        
        # Case 1: Include num at index i (CAN ONLY DO THIS ONCE!)
        candidate = self.candidates[i]
        res.append(candidate)
        self.backtrack(i + 1, cur_sum + candidate, res, candidate)
        res.pop()

        # Case 2: Don't include num at index i. If candidate is same as prev_num,
        # then do NOT consider this case, as it is unnecessary repeated work!!!
        if prev_num != candidate:
            self.backtrack(i + 1, cur_sum, res, prev_num)

        # Since we've covered this solution before, remember this for next time!
        # self.memo.add(tuple_res)

# [1]
# --> [1,1], [1]
# --> [1,1,1], [1,1], [1], [1,1]
# --> [1,1,1,1], [1,1,1], [1,1,1], [1,1], [1,1], [1], [1,1,1], [1,1]

# [1], prev_num = 1
# [1,1],
# [1,1,1]
# [1,1,1,2]