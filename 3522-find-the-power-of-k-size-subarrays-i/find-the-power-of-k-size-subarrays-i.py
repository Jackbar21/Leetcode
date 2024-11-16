class Solution:
    def __init__(self):
        self.memo = {}

    def getPowerArrayLengthFromIndex(self, i, nums):
        if i in self.memo:
            return self.memo[i]

        if i >= len(nums) - 1:
            return 1
        
        res = 1
        if nums[i] == nums[i + 1] - 1:
            res += self.getPowerArrayLengthFromIndex(i + 1, nums)
        
        self.memo[i] = res
        return res
        
        
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
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
            if self.getPowerArrayLengthFromIndex(i, nums) >= k
            else -1
            for i in range(len(nums) - k + 1)
        ]


        answer = []
        n = len(nums)
        for i in range(n - k + 1):
            j = (i + k - 1)
            # print(i, j, self.isSorted(i, j))
            if self.isSorted(nums, i, j):
                answer.append(nums[j])
            else:
                answer.append(-1)
        
        return answer
    
    def isSorted(self, nums, i, j):
        for index in range(i, j):
            if nums[index] != nums[index + 1] - 1:
                return False
        
        return True