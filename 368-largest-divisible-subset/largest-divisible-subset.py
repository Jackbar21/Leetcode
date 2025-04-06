class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.nums = nums
        self.prev = {}

        best_index, best_length = None, float("-inf")
        for i, num in enumerate(nums):
            if (length := self.dp(i)) > best_length:
                best_length = length
                best_index = i

        res = []
        while best_index is not None:
            res.append(nums[best_index])
            best_index = self.prev.get(best_index, None)
        return res
    
    @cache
    def dp(self, i):
        nums = self.nums
        max_num = nums[i]

        # Since array is sorted, look only through indices smaller than i,
        # since that's where all the smaller numbers are located!
        if i < 0:
            return 0

        res = 1
        for j in range(i):
            num = nums[j]
            # assert num < max_num # not '<=' since all numbers distinct!
            if max_num % num == 0:
                case = 1 + self.dp(j) # TODO: max_num might work as well here?
                if res < case:
                    res = case
                    self.prev[i] = j
        
        return res
