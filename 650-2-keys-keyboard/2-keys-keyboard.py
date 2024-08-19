class Solution:
    def __init__(self):
        self.n = None
        self.memo = {}
    def minSteps(self, n: int) -> int:
        self.n = n
        if n <= 1:
            return 0

        # First step is copy step. This is unavoidable
        # Hence we've already "taken" 1 step, with cur_len of 1
        # since 1 'A' on screen, and paste_amount of 1 since we
        # just copied the singular 'A' that is on screen :)
        steps, cur_len, paste_amount = 1, 1, 1
        return steps + self.minStepsDp(cur_len, paste_amount)
    
    def minStepsDp(self, cur_len: int, paste_amount: int) -> int:        
        if cur_len >= self.n:
            # If cur_len > self.n, doesn't matter how many times we copy and/or paste, we will
            # NEVER reach a solution (since we can only grow the number of As, not shrink it!)
            return 0 if cur_len == self.n else float("inf")
        
        if (cur_len, paste_amount) in self.memo:
            return self.memo[(cur_len, paste_amount)]
        
        # Case 1: Choose copy action
        assert cur_len >= paste_amount
        case1 = float("inf") if cur_len == paste_amount else self.minStepsDp(cur_len, cur_len)

        # Case 2: Choose paste option
        case2 = self.minStepsDp(cur_len + paste_amount, paste_amount)

        self.memo[(cur_len, paste_amount)] = 1 + min(case1, case2)
        return self.memo[(cur_len, paste_amount)]