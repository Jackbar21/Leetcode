class Solution:
    def __init__(self):
        self.n = None
        self.memo = {}
    def minSteps(self, n: int) -> int:
        if n <= 1:
            return 0
        
        self.n = n
        # return 

        # First step is copy step. This is unavoidable
        steps = 1
        cur_len = 1
        paste_amount = 1 # Amount than you can paste at the moment
        # just_copied = True # True if last action was 'copy', False if last action was 'paste'
        return steps + self.minStepsDp(cur_len, paste_amount)
    
    def minStepsDp(self, cur_len: int, paste_amount: int) -> int:
        assert self.n >= 1
        if self.n <= 1:
            return 0
        
        if cur_len >= self.n:
            # return steps # TODO: consider removing steps altogether!
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





        
        
