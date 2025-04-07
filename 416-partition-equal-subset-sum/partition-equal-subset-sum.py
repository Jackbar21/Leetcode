class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            # Sum is odd, 100% CANNOT partition it into two equal subsets in sum!
            return False
        
        self.nums = nums
        self.memo = {}
        target_sum = sum_nums // 2
        # return self.dp(0, target_sum)

        self.target_sum = target_sum
        return target_sum in self.dp_1d(0)
    
    def dp_1d(self, i):
        if i >= len(self.nums):
            return set()
        
        num = self.nums[i]

        subset_sums = self.dp_1d(i + 1)
        if self.target_sum in subset_sums:
            # No need to keep making subset_sums larger!
            return [self.target_sum]

        subset_sums.update([subset_sum + num for subset_sum in subset_sums])
        subset_sums.add(num)
        return subset_sums
        
    
    def dp(self, i, sum_left):
        if (i, sum_left) in self.memo:
            return self.memo[(i, sum_left)]

        if sum_left <= 0 or i >= len(self.nums):
            return sum_left == 0
        
        num = self.nums[i]

        # Case 1: Include num
        case1 = self.dp(i + 1, sum_left - num)
        if case1:
            self.memo[(i, sum_left)] = True
            return True

        # Case 2: Don't include num
        case2 = self.dp(i + 1, sum_left)
        if case2:
            self.memo[(i, sum_left)] = True
            return True

        self.memo[(i, sum_left)] = False
        return False