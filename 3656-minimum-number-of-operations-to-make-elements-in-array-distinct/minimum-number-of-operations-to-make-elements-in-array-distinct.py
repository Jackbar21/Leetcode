class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo = {}
        return self.dp(0, len(nums) - 1)

    
    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        nums = self.nums
        # Base Case: Check if nums is already distinct!
        seen = set()
        is_distinct = True
        for index in range(i, j + 1):
            num = nums[index]
            if num in seen:
                is_distinct = False
                break
            seen.add(num)
        if is_distinct:
            return 0
        
        # Case 1: Pop 3 elements from the LEFT
        res = 1 + self.dp(i + 3, j)

        # Case 2: Pop 3 elements from the RIGHT

        self.memo[(i, j)] = res
        return res
