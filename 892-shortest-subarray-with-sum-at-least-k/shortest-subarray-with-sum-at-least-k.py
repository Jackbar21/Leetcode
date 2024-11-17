class Solution:
    # gets sum of nums[i..j] (i.e. INCLUDING index i AND index j!)
    def getSubarraySum(self, i, j):
        # prefix_sums[i] == sum(nums[0..i])
        # ==> sum(nums[i..j]) == prefix_sums[j] - (prefix_sums[i - 1] if i > 0 else 0)
        # return self.prefix_sums[j] - (prefix_sums[i - 1] if i > 0 else 0)
        assert 0 <= i < len(self.nums)
        assert 0 <= j < len(self.nums)
        if i == 0:
            return self.prefix_sums[j]
        
        return self.prefix_sums[j] - self.prefix_sums[i - 1]
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i] # stores left pointer
        
        # Base Case:
        # if i >= len(self.nums):
        #     return 0

        # Case 1: Choose to add index i to current result!
        prev_l = self.dp(i - 1)
        case1 = float("inf")
        if self.getSubarraySum(prev_l, i) >= self.k:
            case1 = i - prev_l + 1

        # Case 2: Choose to make index i beginning of new result!

    # Returns length of shortest non-empty subarray of nums, with sum of at least k
    # (or -1 if none exists), *** that ENDS at index i ***
    def dp_old(self, i):
        if i in self.memo:
            return self.memo[i]
        
        # res = float("inf")
        nums, k = self.nums, self.k
        if i == 0:
            return 1 if nums[i] >= k else -1
        
        prev = self.dp(i - 1)


        
        self.memo[i] = res
        return res

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # if sum(nums) < k:
        #     return -1
        
        # O(n)
        prefix_sums = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sums.append(prefix_sums[-1] + nums[i])
        self.prefix_sums = prefix_sums
        self.nums, self.k = nums, k
        self.memo = {}

        # Min Heap
        # min_heap = [(prefix_sum, i) for i, prefix_sum in enumerate(prefix_sums)]
        # heapq.heapify(min_heap)

        min_heap = []
        SUM, INDEX = 0, 1
        res = float("inf")
        for r in range(len(nums)):
            
            # if prefix_sums[r] < k:
            #     continue
            heapq.heappush(min_heap, (prefix_sums[r - 1] if r > 0 else 0, r))
            # assert prefix_sum >= k
            while (
                len(min_heap) > 0 
                # and min_heap[0][INDEX] <= r 
                and self.getSubarraySum(min_heap[0][INDEX], r) >= k
            ):
                prefix_sum, index = heapq.heappop(min_heap)
                res = min(res, r - index + 1)

            


        return res if res != float("inf") else -1


        # Idea: Go through every index r. You 
        # SUM, INDEX = 0, 1
        # res = float("inf")
        # for r in range(len(nums)):
        #     while (len(min_heap) > 0 
        #         and min_heap[0][INDEX] <= r
        #         and self.getSubarraySum(min_heap[0][INDEX], r) >= k):
        #         prefix_sum, index = heapq.heappop(min_heap)
        #         res = min(res, r - index + 1)

        # d = {
        #     i: prefix_sum
        #     for i, prefix_sum in enumerate(prefix_sums)
        # }
        prefix_sums = sorted([(prefix_sum, i) for i, prefix_sum in enumerate(prefix_sums)])

        res = float("inf")
        for r in range(len(nums)):
            # keys_to_delete = []

            for index in d:
                if index <= r and self.getSubarraySum(index, r) >= k:
                    res = min(res, r - index + 1)
                    keys_to_delete.append(index)

                # Loop Invariant
                # keys_to_delete.append(index)

            for key in keys_to_delete:
                del d[key]

            
        # print(min_heap)
        return res if res != float("inf") else -1

        res = float("inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if self.getSubarraySum(i, j) >= k:
                    res = min(res, j - i + 1)
        
        return res if res != float("inf") else -1

        # l, r

        # l, r --> no point searching for larger r

        # Once I find a valid pair l, r, i.e. such that sum(nums[l..r]) >= k,
        # do I increment l or r? <-- GOLDEN QUESTION

        # Case 1: Increment r
        # Case 2: Increment l

        # cur_sum = 0
        # l = 0
        # res = float("inf")

        # for r in range(len(nums)):
        #     cur_sum = cur_sum + nums[r]
        #     # print(cur_sum, r)

        #     while l <= r and cur_sum >= k:
        #         res = min(res, r - l + 1)
        #         cur_sum -= nums[l]
        #         l += 1
        #         # print("AHHH")
        
        # print(l, r, cur_sum, k, res)
        # while l <= r and cur_sum >= k:
        #     res = min(res, r - l + 1)
        #     cur_sum -= nums[l]
        #     l += 1


        # while l < len(nums):
        #     if cur_sum >= k:
        #         res = min(res, r - l + 1)
        #     cur_sum -= nums[l]
        #     l += 1
        
        l, r = 0, len(nums) - 1
        cur_sum = sum(nums)
        res = float("inf")
        while l <= r:
            if cur_sum >= k:
                res = min(res, r - l + 1)
            if nums[l] < nums[r]:
                cur_sum -= nums[l]
                l += 1
            else:
                cur_sum -= nums[r]
                r -= 1

        print(f"{nums=}")
        print(f"{prefix_sums=}")
        return res if res != float("inf") else -1

        # if nums == [2,-1,2]:
        #     print(self.getSubarraySum(1, 2))
        
        # getSubarrySum(i, j) is now a function that returns the sum
        # between indices i and j in only O(1) time!!!
        return min(
            self.dp(i)
            for i in range(len(nums))
        )
        

        # print(prefix_sums)
        # return 0

        # best solution up to index i-1, can I find best solution for up to index i?
        # Suppose solution to index i-1 is equal to n
        # Case 1: same as best solution up to index i-1 (so n)
        # Case 2: up to 

        # self.memo[i] --> l, r

        # l, r
        # l, r + k

# [84,-37,32,40,95], k= 168, cur_sum = 79
#  l      r

# 