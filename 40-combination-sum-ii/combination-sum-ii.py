class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)
        self.target = target
        self.res = collections.deque()
        self.backtrack(0, 0, [], defaultdict(int))
        return list(set(self.res))
    
    def backtrack(self, i: int, cur_sum: int, res: list, used: dict) -> None:        
        if cur_sum >= self.target or i >= len(self.candidates):
            if cur_sum == self.target:
                self.res.append(tuple(res))
            return

        # Case 1: Include num at index i (CAN ONLY DO THIS ONCE!)
        candidate = self.candidates[i]
        new_sum = cur_sum + candidate
        if new_sum <= self.target:
            # assert candidate not in used
            used[candidate] += 1
            res.append(candidate)
            self.backtrack(i + 1, cur_sum + candidate, res, used)
            res.pop()
            used[candidate] -= 1

        # Case 2: Don't include num at index i. If candidate is same as prev_num,
        # then do NOT consider this case, as it is unnecessary repeated work!!!
        assert used[candidate] >= 0
        if used[candidate] == 0:
            # used[candidate] += 1
            self.backtrack(i + 1, cur_sum, res, used)
            # used[candidate] -= 1

# [a,b,...,z,1] --> [a,b,...,z,1], [a,b,...,z,1,1]
# 