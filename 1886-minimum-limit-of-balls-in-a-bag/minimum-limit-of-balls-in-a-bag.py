class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Given a desired max penalty, we can return how many operations it would take
        # to reach that max penalty! Now, we want to find SMALLEST penalty, such that the 
        # number of operations required to reach this penalty is <= maxOperations. Since the
        # larger the penalty, the less operations are needed and vice versa, we can simply 
        # binary search for the result :)
        l, r = 1, max(nums)
        # res = r # since 0 operations guaranteed to be <= maxOperations!
        while l < r:
            mid = (l + r) // 2 # mid = penalty value itself!
            needed_operations = self.getNumOperationsToReachPenalty(nums, mid)
            if needed_operations <= maxOperations:
                # Then we CAN indeed reach this penalty, so update our
                # result, and now only search for potentially BETTER (i.e. smaller)
                # penalties that might ALSO be valid!
                # res = mid
                r = mid
            else:
                l = mid + 1

        return r
    
    def getNumOperationsToReachPenalty(self, nums, max_penalty):
        # Want to compute how many times we'd need to split the bag to make it such that
        # the HIGHEST penalty in the bag is 'penalty' (the input).
        return sum(math.ceil((num - max_penalty) / max_penalty) for num in nums)
        