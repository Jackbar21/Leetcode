class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Key thing to note:
        #   log(m * n)
        #   == log(m) + log(n)
        #   <= log(m + n) + log(m + n)
        #   == 2 * log(m + n)
        #   \el O(log(m + n))
        # So O(log(m * n)) == O(log(m) + log(n)) == O(log(m + n))

        # O((M+N)), where N = len(nums1), M = len(num2)
        # N, M = len(nums1), len(nums2)
        # i1, i2 = 0, 0
        # nums = []
        # while i1 < N and i2 < M:
        #     num1, num2 = nums1[i1], nums2[i2]
        #     if num1 < num2:
        #         nums.append(num1)
        #         i1 += 1
        #     else:
        #         nums.append(num2)
        #         i2 += 1
        # nums.extend(nums1[i1:] if i1 < N else nums2[i2:])
        # L = len(nums)
        # if L % 2 == 1:
        #     return nums[L // 2]
        # return (nums[L // 2] + nums[-1 + L // 2]) / 2

        self.nums1, self.nums2 = nums1, nums2
        M, N = len(nums1), len(nums2)
        print(f"{sorted(nums1 + nums2)=}")
        L = M + N
        if L % 2 == 1:
            return self.getNumAtTargetIndex(L // 2)
        return (self.getNumAtTargetIndex(L // 2) + self.getNumAtTargetIndex(L // 2 - 1)) / 2
    
    def getNumAtTargetIndex(self, target_index):
        nums1, nums2 = self.nums1, self.nums2
        M, N = len(nums1), len(nums2)
        L = M + N
        assert 0 <= target_index < L
        return sorted(nums1 + nums2)[target_index] 
        
        l1, r1 = 0, M - 1
        l2, r2 = 0, N - 1
        while l1 <= r1 and l2 <= r2: # TODO: Figure out if 'and' or 'or' here later...
            mid1 = (l1 + r1) // 2
            mid2 = (l2 + r2) // 2

            # mid1 and mid2 are indices.
            num1 = nums1[mid1]
            num2 = nums2[mid2]



    def leftmostBinarySearch(self, nums, target):
        # Returns leftmost index of target in nums (or index where target would
        # be if it existed in nums!)
        # Ex. [1,2,3,4,5], target = 2
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            num = nums[mid]
            if num >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

    # Returns number at 'target_index' between nums1 and nums2 in O(log (m+n)) time!
    def helper(self, target_index):
        return self.getNumAtIndex(target_index)

        nums1, nums2 = self.nums1, self.nums2
        N, M = len(nums1), len(nums2)
        L = N + M
        assert 0 <= target_index < L
        # return sorted(nums1 + nums2)[target_index]

        # Base Cases
        if N == 0:
            return nums2[target_index]
        if M == 0:
            return nums1[target_index]

        i = N // 2
        num = nums1[i]
        j = self.leftmostBinarySearch(nums2, num)
        # super_j = self.leftmostBinarySearch(nums2, num + 1)
        index1 = i + j
        # super_index1 = i + super_j
        # if index1 <= target_index <= super_index1:
        if index1 == target_index:
            return num
        
        i = M // 2
        num = nums2[i]
        j = self.leftmostBinarySearch(nums1, num)
        # super_j = self.leftmostBinarySearch(nums1, num + 1)
        index2 = i + j
        # super_index2 = i + super_j
        if index2 == target_index:
            return num
        
        # We've got index1, index2
        print("FAIL")
        return sorted(nums1 + nums2)[target_index]

        # Let's try to get middle element in nums1 and nums2. For each of these,
        # we will get their "true" index. For example, if i = len(nums1) // 2,
        # then we can apply leftmost binary search to f

        
        # # Get to index (N//2)-1
        # N = len(nums1) + len(nums2)
        # index = 0
        # i1, i2 = 0, 0
        # target_index = (N//2) - 1
        # while index < target_index:
        #     if i1 < len(nums1) and nums1[i1] <= nums2[i2]:
        #         i1 += 1
        #     else:
        #         i2 += 1
        #     index += 1
        
        
        
        
        # if N % 2 == 1:
        #     num1 = nums1[i1] if i1 < len(nums1) else nums1[-1] if len(nums1) > 0 else float("-inf")
        #     num2 = nums2[i2] if i2 < len(nums2) else nums2[-1] if len(nums2) > 0 else float("-inf")
        #     if num1 < num2:
        #         i1 += 1
        #     else:
        #         i2 += 1
        #     num1 = nums1[i1] if i1 < len(nums1) else nums1[-1] if len(nums1) > 0 else float("-inf")
        #     num2 = nums2[i2] if i2 < len(nums2) else nums2[-1] if len(nums2) > 0 else float("-inf")
        #     return min(num1, num2)
        
        # num1 = nums1[i1] if i1 < len(nums1) else nums1[-1] if len(nums1) > 0 else float("-inf")
        # num2 = nums2[i2] if i2 < len(nums2) else nums2[-1] if len(nums2) > 0 else float("-inf")
        # return (num1 + num2) / 2
            
        
        # log(m) * log(n)
        # log(m) + log(n) == log(m * n)

        # log(m * n)
        # == log(m) + log(n)
        # <= log(m + n) + log(m + n)
        # == 2 * log(m + n)
        # \el O(log(m + n))

