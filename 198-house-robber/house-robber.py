class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return self.dp(0) # self.dp(i) solves the problem for nums[i:], so we want self.dp(0)!
    
    # O(N) subproblems, O(1) work in body --> O(N*1) == O(N) time complexity!
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        # BRUTE FORCE LOGIC (START)

        # Base Case: No more homes to rob
        if i >= len(self.nums):
            return 0
        
        # Case 1: Rob current house
        case1 = self.nums[i] + self.dp(i + 2)

        # Case 2: Don't rob current house
        case2 = 0 + self.dp(i + 1)

        res = max(case1, case2)

        # BRUTE FORCE LOGIC (END)

        self.memo[i] = res
        return res
    
# dp(0) --ROB--> dp(2) --> ROB --> dp(4) --> ... -->
# dp(0) --NOT-ROB--> dp(1) --NOT-ROB--> dp(2) --> STOP (result already in self.memo!).

# O(2^(n/2))