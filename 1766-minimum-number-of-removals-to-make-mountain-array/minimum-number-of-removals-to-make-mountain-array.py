class Solution:
    def __init__(self):
        self.memo = {}

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        self.memo = {}
        arr1 = [
            self.getNumDeletesFromLIS(i, self.longestIncreasingSubsequence(nums, i))
            for i in range(len(nums))
        ]


        # self.nums = self.nums[::-1]
        # self.memo = {}
        # arr2 = [self.minMovesToMakeArraySorted(i, -1, i + 1) for i in range(len(nums))]
        # arr2 = [self.minDeletesToMakeArraySorted(nums[::-1], i, float("inf"), i + 1) for i in range(len(nums))]
        # arr2 = [self.minDeletes(nums, i, len(nums) - 1) for i in range(len(nums))]

        
        # arr2 = []
        # if not flag:
        #     arr2 = [self.minDeletes1D(reverse_nums, i, float("inf")) for i in range(len(nums))]
        # else:
        #     arr2 = [self.minDeletes2D(reverse_nums, 0, i) for i in range(len(nums))]
        
        self.memo = {}
        reverse_nums = nums[::-1]
        # arr2 = [self.minDeletesLIS(reverse_nums, i) for i in range(len(nums))]
        arr2 = [
            self.getNumDeletesFromLIS(i, self.longestIncreasingSubsequence(reverse_nums, i))
            for i in range(len(nums))
        ]
        # self.nums = self.nums[::-1]

        # print(arr1)
        # arr2 = arr2[::-1]
        # print(arr2[::-1])
        

        res = float("inf")
        for i in range(1, len(nums) - 1):
            # res = min(res, arr1[i] + arr2[len(nums) - 1 - i])
            # if arr1[i] < i and arr2[len(nums) - 1 - i] < len(nums) - 1 - i:
            # if arr1[i] < i and arr2[len(nums) - 1 - i] < len(nums) - 1 - i:
            if arr1[i] < i and arr2[len(nums) - 1 - i] < len(nums) - 1 - i:
                # # print(i)
                # res = min(res, arr1[i] + arr2[i])
                res = min(res, arr1[i] + arr2[len(nums) - 1 - i])
            # res1, num_left1 = arr1[i]
            # res2, num_left2 = arr2[i]
            # if num_left1 + num_left2 >= 3:
            #     res = min(res, res1 + res2)
            
        # return min_moves + res
        return res
    
    def getNumDeletesFromLIS(self, index, lis):
        return (index + 1) - lis
    
    def longestIncreasingSubsequence(self, nums, i):
        if i in self.memo:
            return self.memo[i]

        lis = 1
        for index in range(i):
            if nums[index] < nums[i]:
                case = 1 + self.longestIncreasingSubsequence(nums, index)
                lis = max(lis, case)
        
        self.memo[i] = lis
        return lis
 