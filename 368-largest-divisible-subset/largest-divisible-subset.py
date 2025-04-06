class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        self.nums = nums
        self.memo = {}
        self.prev = {}
        for i, num in enumerate(nums):
            self.dp(i, num)
        print(f"{self.memo=}")
        print(f"{self.prev=}")

        best_index, best_length = None, float("-inf")
        for i, num in enumerate(nums):
            if (length := self.dp(i, num)) > best_length:
                best_length = length
                best_index = i
        
        print(f"{best_index=}")
        res = []
        while best_index is not None:
            res.append(nums[best_index])
            best_index = self.prev.get(best_index, None)
        return res
    
    def dp(self, i, max_num):
        if (i, max_num) in self.memo:
            return self.memo[(i, max_num)]

        # Since array is sorted, look only through indices smaller than i,
        # since that's where all the smaller numbers are located!
        nums = self.nums
        if i < 0:
            return 0

        res = 1
        for j in range(i):
            num = nums[j]
            assert num < max_num # not '<=' since all numbers distinct!
            if max_num % num == 0:
                case = 1 + self.dp(j, num) # TODO: max_num might work as well here?
                if res < case:
                    res = case
                    self.prev[i] = j
        
        self.memo[(i, max_num)] = res
        return res

        
