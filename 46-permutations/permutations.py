class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], collections.deque(nums))
        return self.res
    
    def backtrack(self, permutation, remaining_nums):
        if len(remaining_nums) == 0:
            self.res.append(permutation.copy())
            return

        for i in range(len(remaining_nums)):
            num = remaining_nums.popleft()
            permutation.append(num)
            self.backtrack(permutation, remaining_nums)
            permutation.pop()
            remaining_nums.append(num)
