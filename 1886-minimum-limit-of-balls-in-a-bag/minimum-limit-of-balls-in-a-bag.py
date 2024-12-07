class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        # Given a desired max penalty, we can return how many operations it would take
        # to reach that max penalty!
        self.nums = nums

        # Now, we want to find SMALLEST penalty, such that the number of operations
        # required to reach this penalty is <= maxOperations. Since the larger the penalty,
        # the less operations are needed and vice versa, we can simply binary search for the
        # result :)
        l, r = 1, max(self.nums)
        res = r # since 0 operations guaranteed to be <= maxOperations!
        while l <= r:
            mid = (l + r) // 2 # mid = penalty value itself!
            needed_operations = self.getNumOperationsToReachPenalty(mid)
            if needed_operations <= maxOperations:
                # Then we CAN indeed reach this penalty, so update our
                # result, and now only search for potentially BETTER (i.e. smaller)
                # penalties that might ALSO be valid!
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        # res = self.getNumOperationsToReachPenalty(3)
        return res
    
    def getNumOperationsToReachPenalty(self, max_penalty):
        # Want to compute how many times we'd need to split the bag to make it such that
        # the HIGHEST penalty in the bag is 'penalty' (the input).
        res = 0
        for num in self.nums:
            res += math.ceil((num - max_penalty) / max_penalty)
        return res
        
        max_heap = self.max_heap.copy()
        num_operations = 0
        while -max_heap[0] > max_penalty:
            penalty = -heapq.heappop(max_heap)

            bag1 = max_penalty
            bag2 = penalty - bag1
            heapq.heappush(max_heap, -bag1)
            heapq.heappush(max_heap, -bag2)
            num_operations += 1
        
        return num_operations
