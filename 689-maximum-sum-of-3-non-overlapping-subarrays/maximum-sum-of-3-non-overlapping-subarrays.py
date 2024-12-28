class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        cur_sum = sum(nums[i] for i in range(k)) # == sum(nums[0..k-1])
        prefix_sums = [cur_sum]
        l = 0
        for r in range(k, len(nums)):
            cur_sum -= nums[l]
            l += 1
            cur_sum += nums[r]
            prefix_sums.append(cur_sum)
        
        print(f"{prefix_sums=}")
        # return []
        self.nums = nums
        self.k = k
        self.prefix_sums = prefix_sums
        self.memo = {}
        # return self.dp(0, ())
        return self.fastDp(0, 3)
    
    def getSumFromIndices(self, indices):
        # assert len(indices) == 3
        return sum(self.prefix_sums[index] for index in indices)
    
    def fastDp(self, i, indices_left):
        assert indices_left >= 0
        if indices_left == 0:
            return ()

        if (i, indices_left) in self.memo:
            return self.memo[(i, indices_left)]
        
        if i > len(self.nums) - self.k:
            return float("-inf") # since indices_left > 3
            # return ()
        
        # Case 1: Choose index i
        case1 = self.fastDp(i + self.k, indices_left - 1)
        if case1 != float("-inf"):
            case1 = tuple([i] + list(case1))
        print(f"{case1=}")
        case1_sum = case1 if case1 == float("-inf") else self.getSumFromIndices(case1)
        

        # Case 2: Skip index i
        case2 = (self.fastDp(i + 1, indices_left))
        if case2 != float("-inf"):
            case2 = tuple(case2)
        print(f"{case2=}")
        case2_sum = case2 if case2 == float("-inf") else self.getSumFromIndices(case2)

        if case1_sum > case2_sum:
            self.memo[(i, indices_left)] = case1
            return tuple(case1)
        elif case2_sum > case1_sum:
            self.memo[(i, indices_left)] = case2
            return tuple(case2)
        
        # Otherwise, since they are equal, we must return the lexicographically smallest one
        # self.memo[i] = case1 if case1 < case2 else case2
        # return self.memo[i]

        self.memo[(i, indices_left)] = (case1) if case1 < case2 else (case2)
        return self.memo[(i, indices_left)]

    
    def dp(self, i, indices):
        if (i, indices) in self.memo:
            return self.memo[i]

        assert len(indices) <= 3
        if len(indices) == 3:
            # self.memo[(i, indices)] = indices # O(1)
            return indices

        if i > len(self.nums) - self.k:
            # return float("-inf") # since len(indices) != 3
            self.memo[(i, indices)] = float("-inf")
            return float("-inf")

        # Case 1: Choose index i
        new_indices = tuple(list(indices) + [i])
        case1 = self.dp(i + self.k, new_indices)
        case1_sum = case1 if case1 == float("-inf") else self.getSumFromIndices(case1)

        # Case 2: Skip index i
        case2 = self.dp(i + 1, indices)
        case2_sum = case2 if case2 == float("-inf") else self.getSumFromIndices(case2)
        
        if case1_sum > case2_sum:
            self.memo[(i, indices)] = case1
            return case1
        elif case2_sum > case1_sum:
            self.memo[(i, indices)] = case2
            return case2
        
        # Otherwise, since they are equal, we must return the lexicographically smallest one
        # self.memo[i] = case1 if case1 < case2 else case2
        # return self.memo[i]
        self.memo[(i, indices)] = case1 if case1 < case2 else case2
        return self.memo[(i, indices)]