class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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

        L = len(nums1) + len(nums2)
        self.L, self.nums1, self.nums2 = L, nums1, nums2
        
        if L % 2 == 1:
            return self.helper(L // 2)
        return (self.helper(L // 2) + self.helper(L // 2 - 1)) / 2

    # Returns number at 'target_index' between nums1 and nums2 in O(log (m+n)) time!
    def helper(self, target_index):
        L, nums1, nums2 = self.L, self.nums1, self.nums2
        assert 0 <= target_index < L
        return sorted(nums1 + nums2)[target_index]

        
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
            