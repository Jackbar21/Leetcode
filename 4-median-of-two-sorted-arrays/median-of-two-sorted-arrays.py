class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.findMedianSortedArraysBAD(nums1, nums2)
        M, N = len(nums1), len(nums2)
        half = (M + N) // 2
        nums1, nums2 = (nums1, nums2) if M < N else (nums2, nums1)
        # nums1, nums2 = nums1, nums2

        # Binary search on the number of elements to take FROM nums1
        l, r = 0, len(nums1)
        # print(f"{l,r,nums1==nums1=}")
        magic_x = None
        while l <= r:
            x = (l + r) // 2
            # print(f"{x=}")
            a_max_left = nums1[x - 1] if x - 1 >= 0 else float("-inf")
            a_min_right = nums1[x] if x < len(nums1) else float("inf")
            b_max_left = nums2[half - x - 1] if half - x - 1 >= 0 else float("-inf")
            b_min_right = nums2[half - x] if half - x < len(nums2) else float("inf")
            
            # print(f"{a_max_left, a_min_right=}")
            assert a_max_left <= a_min_right
            # print(f"{b_max_left, b_min_right=}")
            assert b_max_left <= b_min_right
            if a_max_left <= b_min_right and b_max_left <= a_min_right:
                # print(f"VALID SOLUTION")
                magic_x = x
                break
            
            if a_max_left <= b_min_right:
                assert not (b_max_left <= a_min_right)
                l = x + 1
                continue
            
            assert not (a_max_left <= b_min_right)
            r = x - 1
            continue

        min_right = min(
            nums1[x] if x < len(nums1) else float("inf"),
            nums2[half - x] if half - x < len(nums2) else float("inf")
        )
        assert min_right != float("inf")
        if (M + N) % 2 == 1:
            return min_right
        
        # Since total merged length is even, need to take average of two median elements
        max_left = max(
            nums1[x - 1] if x - 1 >= 0 else float("-inf"),
            nums2[half - x - 1] if half - x - 1 >= 0 else float("-inf")
        )
        assert max_left != float("-inf")
        return (min_right + max_left) / 2
            



    
    def findMedianSortedArraysBAD(self, nums1: List[int], nums2: List[int]) -> float:
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
        # # print(f"{sorted(nums1 + nums2)=}")
        L = M + N
        if L % 2 == 1:
            return self.getNumAtTargetIndex(L // 2)
        return (self.getNumAtTargetIndex(L // 2) + self.getNumAtTargetIndex(L // 2 - 1)) / 2
    
    # O(log(m) + log(n)) [which we've proved is same as O(log(m + n))]
    def countGreaterThan(self, num):
        nums1, nums2 = self.nums1, self.nums2
        M, N = len(nums1), len(nums2)
        L = M + N
        res = 0

        # Greater than in nums1 array -- O(log(M))
        # Find rightmost index i such that nums1[i] < num,
        # and count greater than will be i + 1.
        l1, r1 = 0, M - 1
        rightmost = None
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if nums1[m1] < num:
                # Valid solution, look for larger ones
                rightmost = m1
                l1 = m1 + 1
            else:
                r1 = m1 - 1
        if rightmost is not None:
            res += rightmost + 1
        
        # Greater than in nums2 array -- O(log(N))
        # Find rightmost index i such that nums2[i] < num,
        # and count greater than will be i + 1.
        l2, r2 = 0, N - 1
        rightmost = None
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if nums2[m2] < num:
                # Valid solution, look for larger ones
                rightmost = m2
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        if rightmost is not None:
            res += rightmost + 1
        
        return res

    # O(log(m) + log(n)) [which we've proved is same as O(log(m + n))]
    def countGreaterThanOrEqualTo(self, num):
        nums1, nums2 = self.nums1, self.nums2
        M, N = len(nums1), len(nums2)
        L = M + N
        res = 0

        # Greater than in nums1 array -- O(log(M))
        # Find rightmost index i such that nums1[i] <= num,
        # and count greater than will be i + 1.
        l1, r1 = 0, M - 1
        rightmost = None
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if nums1[m1] <= num:
                # Valid solution, look for larger ones
                rightmost = m1
                l1 = m1 + 1
            else:
                r1 = m1 - 1
        if rightmost is not None:
            res += rightmost + 1
        
        # Greater than in nums2 array -- O(log(N))
        # Find rightmost index i such that nums2[i] <= num,
        # and count greater than will be i + 1.
        l2, r2 = 0, N - 1
        rightmost = None
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if nums2[m2] <= num:
                # Valid solution, look for larger ones
                rightmost = m2
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        if rightmost is not None:
            res += rightmost + 1
        
        return res

    
    def getNumAtTargetIndex(self, target_index):
        nums1, nums2 = self.nums1, self.nums2
        M, N = len(nums1), len(nums2)
        L = M + N
        assert 0 <= target_index < L
        # return sorted(nums1 + nums2)[target_index] 

        
        l1, r1 = 0, M - 1
        l2, r2 = 0, N - 1
        while l1 <= r1 and l2 <= r2:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            # print(f"{l1,r1,m1=}, {l2,r2,m2=}")

            # [2,3,7,7,7,9,10]
            #        m1
            # [1,2,2,3,4,9,10]
            #        m2
            # nums1[m1] >= nums2[m2]
            # nums1[m1] >= at least m1 + m2 + 1 numbers == 3 + 3 + 1 == 7 numbers (so min. at index 8)
            # target_index < 8 --> set r1 = m1 - 1, set r2 = m2
            # target_index >= 8 --> set l1 = m1, l2 = m2 + 1
            num1, num2 = nums1[m1], nums2[m2]
            if num1 >= num2:
                num1_gte_count = m1 + m2 + 1
                num1_min_index = num1_gte_count + 1
                if target_index < num1_min_index:
                    r1 = m1 - 1
                    r2 = m2 #- 1
                elif target_index > num1_min_index:
                    l1 = m1 #+ 1
                    l2 = m2 + 1
                else:
                    return num1
            else:
                # [1,2,2,3,4,9,10]
                #        m1
                # [2,3,7,7,7,9,10]
                #        m2
                # nums2[m2] >= nums1[m1]
                # nums2[m2] >= at least m1 + m2 + 1 numbers == 3 + 3 + 1 == 7 numbers (so min. at index 8)
                # target_index < 8 --> set r1 = m1 - 1, set r2 = m2
                # target_index >= 8 --> set l1 = m1, l2 = m2 + 1
                num2_gte_count = m1 + m2 + 1
                num2_min_index = num2_gte_count + 1
                if target_index < num2_min_index:
                    r1 = m1 #- 1
                    r2 = m2 - 1
                elif target_index > num2_min_index:
                    l1 = m1 + 1
                    l2 = m2 #+ 1
                else:
                    return num2
                
        
        # print(f"{l1,r1,l2,r2=}")
        # raise Exception("hehe")
        return nums1[l1] if l1 > r1 else nums2[l2]
        
        # ATTEMPT 1:
        l1, r1 = 0, M - 1
        l2, r2 = 0, N - 1
        while l1 <= r1 and l2 <= r2: # TODO: Figure out if 'and' or 'or' here later...
            mid1 = (l1 + r1) // 2
            mid2 = (l2 + r2) // 2

            # mid1 and mid2 are indices.
            num1 = nums1[mid1]
            num2 = nums2[mid2]

            # [2,3,6,7,9,9,10]
            #        m1
            # [1,2,2,3,4,9,10]
            #        m2
            # nums1[m1] >= nums2[m2]
            # nums1[m1] >= at least m1 + m2 + 1 numbers == 3 + 3 + 1 == 7 numbers (so min. at index 8)
            # target_index > 8 --> look to right of m2 (e.g. l2 = m2 + 1)
            # target_index < 8 --> look to left of m1 (e.g. r1 = m1 - 1)
            # target_index == 8 --> return nums1[m1] X
            #       can't do this since m1 is AT LEAST at index 8. But can definitely ignore anything <m1

            m1, m2 = mid1, mid2
            if num1 >= num2:
                num1_greater_than_count = m1 + m2 + 1
                num1_index = num1_greater_than_count + 1
                # if num1 == num2 and target_index == num1_index - 1:
                #     return num1
                if target_index > num1_index:
                    l2 = m2 + 1
                elif target_index < num1_index:
                    r1 = m1 - 1
                else:
                    assert target_index == num1_index
                    # return num1
                    l1 = m1
            elif num1 < num2:
                # [2,3,6,7,9,9,10]
                #        m1
                # [1,2,2,3,4,9,10]
                #        m2
                # nums1[m1] >= nums2[m2]
                # nums1[m1] >= at least m1 + m2 + 1 numbers == 3 + 3 + 1 == 7 numbers (so min. at index 8)
                # target_index > 8 --> look to right of m2 (e.g. l2 = m2 + 1)
                # target_index < 8 --> look to left of m1 (e.g. r1 = m1 - 1)
                # target_index == 8 --> return nums1[m1]
                num2_greater_than_count = m2 + m1 + 1
                num2_index = num2_greater_than_count + 1
                if target_index > num2_index:
                    l1 = m1 + 1
                elif target_index < num2_index:
                    r2 = m2 - 1
                else:
                    assert target_index == num2_index
                    # return num2
                    # l1 = m1
                    l2 = m2
            # else:
            #     assert num1 == num2
            #     possible_indices = [m1 + m2, m1 + m2 + 1]
            #     if target_index in possible_indices:
            #         return num1
            #     num_index = m1 + m2 + 1
            #     # Randomly choose to binary search first array? Maybe can do smaller array?
            #     # Bigger array? Idk... guessing it doesn't matter?
            #     if target_index > num_index:
            #         l1 = m1 + 1
            #         l2 = m2 + 1
            #     else:
            #         assert target_index < m1 + m2
            #         r1 = m1 - 1
            #         r2 = m2 - 1

        # print(f"{l1,r1,l2,r2=}")
        if l1 == r1:
            return nums1[l1]
        # assert l2 == r2
        return nums2[l2]
        raise Exception("Ended while loop!")


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
        # print("FAIL")
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

# [2,3,6,7,9,9,10]
#        m1

# [1,2,2,3,4,9,10]
#        m2

# nums1[m1] >= nums2[m2]
# nums1[m1] >= at least m1 + m2 + 1 numbers == 3 + 3 + 1 == 7 numbers (so min. at index 8)
# target_index > 8 --> look to right of m2 (e.g. l2 = m2 + 1)
# target_index < 8 --> look to left of m1 (e.g. r1 = m1 - 1)
# target_index == 8 --> return nums1[m1]

# EITHER:
# (1) O(1) total O(log(m + n)) calls
# (2) O(log(m + n)) total O(1) calls

# [2,3,7,7,7,9,10]
#        m1
# [1,2,2,3,4,9,10]
#        m2
# nums1[m1] >= nums2[m2]
# nums1[m1] >= at least m1 + m2 + 1 numbers == 3 + 3 + 1 == 7 numbers (so min. at index 8)
# target_index < 8 --> set r1 = m1 - 1, set r2 = m2
# target_index >= 8 --> set l1 = m1, l2 = m2 + 1


        # # New attempt
        # l = min(num1[0], nums2[0])
        # r = max(nums1[-1], nums2[-1])

        # # Want to find first index
        # # TAKING nums1 BREAK HERE AT THIS POINT... I can't figure this out yet :/ At least made some progress!

        # # O(log(m) * log(n)), which is INVALID. But, might be able to make improvements later on...
        # l, r = 0, M - 1
        # # l2, r2 = 0, N - 1
        # # while l1 <= r1 and l2 <= r2:
        # while l <= r:
        #     m = (l + r) // 2
        #     num = nums1[m]

        #     l1, r1 = m, r
        #     rightmost = m
        #     while l1 <= r1:
        #         m1 = (l1 + r1) // 2
        #         if nums1[m1] == num:
        #             # Valid solution, look for rightmost one
        #             rightmost = m1
        #             l1 = m1 + 1
        #         else:
        #             r1 = m1 - 1


        #     m1 = rightmost
        #     num1 = nums1[m1]
        #     num1_greater_than_or_equal_to_count = m1
        #     # Find rightmost index i in nums2 such that nums2[i] <= num1
        #     # But if nums2[i] > num1 for all i, no such index exists.
        #     # Hence, only binary search if num1 >= nums2[0], i.e.
        #     # the smallest number in nums2.
        #     rightmost_gt = None
        #     rightmost_gte = None
        #     if True or nums2[0] <= num1:
        #         # rightmost_index = None
        #         l2, r2 = 0, N - 1
        #         while l2 <= r2:
        #             m2 = (l2 + r2) // 2
        #             if nums2[m2] <= num1:
        #                 # Valid solution, update rightmost index
        #                 # Search for better solution in right side
        #                 # rightmost_index = m2
        #                 rightmost_gte = m2
        #                 l2 = m2 + 1
        #             else:
        #                 # Invalid solution, look for existing solutions in left side
        #                 r2 = m2 - 1
        #         l2, r2 = 0, N - 1
        #         while l2 <= r2:
        #             m2 = (l2 + r2) // 2
        #             if nums2[m2] < num1:
        #                 # Valid solution, update rightmost index
        #                 # Search for better solution in right side
        #                 # rightmost_index = m2
        #                 rightmost_gt = m2
        #                 l2 = m2 + 1
        #             else:
        #                 # Invalid solution, look for existing solutions in left side
        #                 r2 = m2 - 1
        #         # assert rightmost_index is not None
        #         # num1_greater_than_or_equal_to_count += rightmost_index + 1


        #     upper_bound = num1_greater_than_or_equal_to_count + (rightmost_gte + 1 if rightmost_gte else 0)
        #     lower_bound = num1_greater_than_or_equal_to_count + (rightmost_gt + 1 if rightmost_gt else 0)
        #     # # print(f"{lower_bound=}, {upper_bound=}")
        #     assert lower_bound <= upper_bound
        #     if lower_bound <= target_index <= upper_bound:
        #         return num1
        #     # num1_index = num1_greater_than_or_equal_to_count + 1
        #     num1_index = upper_bound
        #     if target_index < num1_index:
        #         r1 = m1 - 1
        #     elif target_index > num1_index:
        #         l1 = m1 + 1
        #     else:
        #         assert False
        #         assert target_index == num1_index
        #         return num1
        
        # # # print(f"{l1,r1,l2,r2=}")
        # raise Exception("Too bad so sad, time for INVALID SOLUTIONNNNN")

# [2,3,6] [7,9,9,10]
# [1,2,2,3,4] [9,10]


# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
# x = 2
# [1, 2] [3, 4, 5]
# [1,2,3,4] [5,6,7,8]

"""
For example, consider the arrays nums1 = [1, 2, 3, 4, 5] and nums2 = [1, 2, 3, 4, 5, 6, 7, 8]. When we select x = 2, we take 4 elements from array nums2. However, this partition is not valid because value 4 from the left partition of array nums2 is greater than the value 3 from the right partition of array nums1. So, we should try to take more elements from array nums1 to make the partition valid. Binary search will eventually help us find a valid partition.

[1,2,3,4,5]
[1,2,3,4,5,6,7,8]
x = 2

[1,2] [3,4,5]
[1,2,3,4] [5,6,7,8]
"""