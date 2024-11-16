class Solution:
    def __init__(self):
        self.nums = None
        self.k = None
        self.memo = {}

    def dp(self, i):
        nums, k = self.nums, self.k

        if i >= len(nums) - 1:
            return 1
        
        if i in self.memo:
            return self.memo[i]
        
        res = float("-inf")
        if nums[i] <= nums[i + 1]:
            res = 1 + self.dp(i + 1)
        else:
            res = 0
        
        self.memo[i] = res
        return res

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        self.nums, self.k = nums, k
        # lengths = []
        # # for i in range(len(nums) - 1):
        # #     if nums[i] <= nums[i + 1]:
        # #         leng
        # self.dp(0)
        # for key in sorted(self.memo):
        #     print(key, self.memo[key])

        answer = []
        n = len(nums)
        for i in range(n - k + 1):
            j = (i + k - 1)
            # print(i, j, self.isSorted(i, j))
            if self.isSorted(i, j):
                answer.append(nums[j])
            else:
                answer.append(-1)
        
        return answer
    
    def isSorted(self, i, j):
        for index in range(i, j):
            if self.nums[index] != self.nums[index + 1] - 1:
            # if self.nums[index] >= self.nums[index + 1]:
                return False
        
        return True