class Solution:
    def __init__(self):
        self.memo = {0: set([0])}
        self.target = None
        self.nums = None
    
    def canPartDp(self, i):
        if i in self.memo:
            # TODO: !!! FIX RETURN VALUE !!!
            return self.memo[i]
        
        # is there a partition in nums[:i+1] that
        # sums up to target, given all partitions
        # that nums[:i] sum up to?

        partitions = self.canPartDp(i - 1)
        if partitions == True:
            return True # true for i --> true for i+k, k > 0
        new_partitions = set()
        for p in partitions:
            new_partitions.add(p)
            new_partitions.add(p + self.nums[i])

        self.memo[i] = new_partitions if self.target not in new_partitions else True
        return self.memo[i]

    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        
        # Partition into two equal subset sums,
        # means that sum1 + sum2 == sum(nums)
        # where sum1 == sum2, which implies
        # --> sum1 + sum1 == sum(nums)
        # --> 2 * sum1 == sum(nums)
        # --> sum1 == sum(nums)//2
        # --> sum2 == sum(nums)//2
        self.target = sum_nums // 2
        self.nums = nums
        
        # Needed since returns set if not True
        # (not 'False')
        if self.canPartDp(len(nums)-1) == True:
            return True
        return False


