class Solution:
    def __init__(self):
        # self.nums = None
        self.memo = {}

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        print(f"LEN OF NUMS={len(nums)}, MAX DIGIT NUM = len({sorted(nums, key=lambda num: len(str(num)), reverse=True)[0]})={len(str(sorted(nums, key=lambda num: len(str(num)), reverse=True)[0]))}")
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
    
    def minDeletesLIS(self, nums, i):
        # Find LIS that ends at index i
        lis = 0
        # for index in range(i - 1, -1, -1):
        for index in range(i):
            if nums[index] < nums[i]:
                case = 1 + self.minDeletesLIS(nums, index)
                lis = max(lis, case)
        
        self.memo[i] = i + 1 - lis # num deletes!
        return self.memo[i]
    
    def minDeletes2D(self, nums, l, r):
        if (l, r) in self.memo:
            return self.memo[(l, r)]
        
        # if l >= r:
        #     return 1 if nums[l] < 
        if l >= r:
            return 0
        
        # Case 1: Left Index (delete or keep... can only keep if l + 1 index is LARGER value)
        case1 = 1 + self.minDeletes2D(nums, l + 1, r) # delete left index
        if l + 1 < len(nums) and nums[l] < nums[l + 1]:
            case1 -= 1 # keep left index
        
        # Case 2: Right Index (delete or keep... can only keep if r - 1 index is SMALLER value)
        case2 = 1 + self.minDeletes2D(nums, l, r - 1) # delete left index
        if r - 1 >= 0 and nums[r - 1] < nums[r]:
            case2 -= 1 # keep left index
        
        res = min(case1, case2)
        self.memo[(l, r)] = res
        return res
        
        # Case 1: delete left index
        case1 = 1 + self.minDeletes2D(nums, l + 1, r)

        # Case 2: delete right index
        case2 = 1 + self.minDeletes2D(nums, l, r - 1)

        # Case 3: keep left index
        # Can only do so if adjacent index has LARGER value
        case3 = float("inf")
        if l + 1 < len(nums) and nums[l] < nums[l + 1]:
            case3 = self.minDeletes2D(nums, l + 1, r)

        # Case 4: keep right index
        # Can only do so if adjacent index has SMALLER value
        case4 = float("inf")
        if r-1 >= 0 and nums[r - 1] < nums[r]:
            case4 = self.minDeletes2D(nums, l, r - 1)
        
        res = min(case1, case2, case3, case4)
        self.memo[(l, r)] = res
        return res
    
    def minDeletes1D(self, nums, i, max_val):
        if (i, max_val) in self.memo:
            return self.memo[(i, max_val)]
        
        if i < 0:
            return 0
        
        # Case 1: Keep num at index i
        # Can ONLY do this, if num at index i is <= max_val
        case1 = float("inf")
        if nums[i] <= max_val:
            case1 = self.minDeletes1D(nums, i - 1, min(max_val, nums[i] - 1))

        # Case 2: Delete num at index i
        case2 = 1 + self.minDeletes1D(nums, i - 1, max_val)

        res = min(case1, case2)
        self.memo[(i, max_val)] = res
        return res

    def minDeletes(self, nums, l, r, max_val):
        if (l, r) in self.memo:
            return self.memo[(l, r)]
        
        if l >= r:
            return 0 # Problem solved!
        
        # Case 1: Delete left index
        # Case 2: Delete right index
        # Case 3: Keep left index
        # Case 4: Keep right index

        case1 = self.minDeletes(nums, l + 1, r)
        case2 = self.minDeletes(nums, l, r - 1)

        # At least one of the left or the right needed to be deleted,
        # so increment min_deletes by 1.
        min_deletes = min(case1, case2)
        min_deletes += nums[l] >= nums[r]
        # if not nums[l] < nums[r]:
            
        #     min_deletes += 1
        
        self.memo[(l, r)] = min_deletes
        return min_deletes
    
    def minDeletesToMakeArraySorted(self, nums, i, max_val, num_left):
        # Make array up to index i strictly increasing. Max val is used
        # to denote max value for remaining indices (0..i-1) if choose
        # to SELECT and SOLIDIFY choice at index i
        if (i, max_val, num_left) in self.memo:
            return self.memo[(i, max_val, num_left)]
        
        if i < 0:
            # Problem solved!
            return (0, num_left)
        
        # Case 1: Keep element at index i
        # Can ONLY do this, if keeps array sorted!
        # We check this via max_val
        case1 = float("inf")
        if self.nums[i] <= max_val:
            case1 = self.minDeletesToMakeArraySorted(nums, i - 1, min(max_val, self.nums[i] - 1), num_left)[0]

        # Case 2: Delete element at index i
        case2 = float("inf")
        # if num_left > 3:
        case2 = 1 + (self.minDeletesToMakeArraySorted(nums, i - 1, max_val, num_left - 1))[0]
        if case2 < case1 and num_left - 1 < 3:
            print("ALERT!")

        res = min(case1, case2)
        self.memo[(i, max_val, num_left)] = (res, num_left if case1 >= case2 else num_left - 1)
        return self.memo[(i, max_val, num_left)]
        
    def minMovesToMakeArraySorted(self, i, prev_index, num_left):
        # Returns min. # of moves to make array sorted.
        # If prev_index == -1, this indicates no n
        if (i, prev_index, num_left) in self.memo:
            return self.memo[(i, prev_index, num_left)]

        if i >= len(self.nums):
            # Problem complete!
            return 0

        # Case 1: self.nums[i - 1] < self.nums[i]
        # Here, I can choose to greedily NOT delete ANYTHING.
        # In other words, I can choose to KEEP index i
        case1 = float("inf")
        if prev_index == -1 or self.nums[i - 1] < self.nums[i]:
            case1 = self.minMovesToMakeArraySorted(i + 1, i, num_left)
        
        # Case 2: Delete self.nums[i], even if it's potentially
        # ALREADY the case that self.nums[i - 1] < self.nums[i] !
        # But, can only delete if remaining array length is at least 3.
        case2 = float("inf")
        if num_left > 3:
            case2 = 1 + self.minMovesToMakeArraySorted(i + 1, prev_index, num_left - 1)
        
        res = min(case1, case2)
        self.memo[(i, prev_index, num_left)] = res
        return res

# [100,92,89,77,74,66,64,66,64]
# [100,92,89,77,74,66]