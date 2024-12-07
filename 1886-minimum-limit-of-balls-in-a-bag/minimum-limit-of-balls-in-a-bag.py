class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Given a desired max penalty, we can return how many operations it would take
        # to reach that max penalty! Now, we want to find SMALLEST penalty, such that the 
        # number of operations required to reach this penalty is <= maxOperations. Since the
        # larger the penalty, the less operations are needed and vice versa, we can simply 
        # binary search for the result :)
        l, r = 1, max(nums)
        while l < r:
            mid_penalty = (l + r) // 2
            needed_operations = self.getNumOperationsToReachPenalty(nums, mid_penalty)
            if needed_operations <= maxOperations:
                # Then we CAN indeed reach this penalty, so update our
                # result, and now only search for potentially BETTER (i.e. smaller)
                # penalties that might ALSO be valid!
                r = mid_penalty
            else:
                l = mid_penalty + 1

        return r
    
    def getNumOperationsToReachPenalty(self, nums, max_penalty):
        # Want to compute how many times we'd need to split the bag to make it such that
        # the HIGHEST penalty in the bag is 'penalty' (the input).
        res = 0
        for num in nums:
            res += math.ceil((num - max_penalty) / max_penalty)
        return res
