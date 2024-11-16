class Solution:
    @cache
    def getPowerArrayLengthFromIndex(self, i):
        nums = self.nums
        if i >= len(nums) - 1:
            return 1
        
        res = 1
        if nums[i] == nums[i + 1] - 1:
            res += self.getPowerArrayLengthFromIndex(i + 1)
        
        return res
        
        
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        self.nums = nums
        # Idea: from each index, store the length of the LONGEST consecutive & sorted
        # sequence of elements STARTING at that index. Then from that point on, for each
        # index, we check if there is a sorted array of length AT LEAST k (and add its
        # power to answer result if so), or add -1 to answer array since not a power array.
        # print([
        #     self.getPowerArrayLengthFromIndex(i)
        #     for i in range(len(nums))
        # ])
        
        # answer = []
        # n = len(nums)
        # for i in range(n - k + 1):
        #     length = self.getPowerArrayLengthFromIndex(i, nums)
        #     if length >= k:
        #         answer.append(nums[i] + k - 1)
        #     else:
        #         answer.append(-1)
        # return answer
        return [
            (nums[i] + k - 1) 
            if self.getPowerArrayLengthFromIndex(i) >= k
            else -1
            for i in range(len(nums) - k + 1)
        ]
