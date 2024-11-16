class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
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