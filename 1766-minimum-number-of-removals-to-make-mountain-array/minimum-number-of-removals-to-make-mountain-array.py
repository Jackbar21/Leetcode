class Solution:
    def __init__(self):
        # self.nums = None
        self.memo = {}

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # print(f"LEN OF NUMS={len(nums)}, MAX DIGIT NUM = len({sorted(nums, key=lambda num: len(str(num)), reverse=True)[0]})={len(str(sorted(nums, key=lambda num: len(str(num)), reverse=True)[0]))}")
        # No matter what, all duplicates must be removed. Hence, first
        # perform a one-way sweep of nums to get rid of all duplicates
        # seen = set()
        # unique_nums = []
        # min_moves = 0
        # for num in nums:
        #     if num not in seen:
        #         unique_nums.append(num)
        #         min_moves += 1
        #     seen.add(num)
        # self.nums = unique_nums
        # nums = unique_nums
        # self.nums = nums
        # reverse_nums = nums[::-1]

        # res = 0
        # for i in range(1, len(arr) - 1):
        #     left = self.minMovesToMakeArraySorted(i, None)
        #     right = self.minMovesToMakeArraySorted()

        # Return 0 if already not mountain array
        # if len(nums) < 3:
        #     return 0
        
        # arr1 = [self.minMovesToMakeArraySorted(i, -1, i + 1) for i in range(len(nums))]
        # arr1 = [self.minDeletesToMakeArraySorted(nums, i, float("inf"), i + 1) for i in range(len(nums))]
        # arr1 = [self.minDeletes(nums, 0, i) for i in range(len(nums))]
        # flag = False # False if want 1D, True if want 2D
        # arr1 = []
        # if not flag:
        #     arr1 = [self.minDeletes1D(nums, i, float("inf")) for i in range(len(nums))]
        # else:
        #     arr1 = [self.minDeletes2D(nums, 0, i) for i in range(len(nums))]
        
        self.memo = {}
        # arr1 = [self.minDeletesLIS(nums, i) for i in range(len(nums))]
        arr1 = [
            self.getNumDeletesFromLIS(i, self.longestIncreasingSubsequence(nums, i))
            for i in range(len(nums))
        ]
        print(self.memo)


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

        print(arr1)
        # arr2 = arr2[::-1]
        print(arr2[::-1])
        

        res = float("inf")
        for i in range(1, len(nums) - 1):
            # res = min(res, arr1[i] + arr2[len(nums) - 1 - i])
            # if arr1[i] < i and arr2[len(nums) - 1 - i] < len(nums) - 1 - i:
            # if arr1[i] < i and arr2[len(nums) - 1 - i] < len(nums) - 1 - i:
            if arr1[i] < i and arr2[len(nums) - 1 - i] < len(nums) - 1 - i:
                # print(i)
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
 