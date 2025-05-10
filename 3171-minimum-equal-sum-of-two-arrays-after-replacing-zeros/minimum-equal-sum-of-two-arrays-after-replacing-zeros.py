class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_count1 = sum(num == 0 for num in nums1)
        zero_count2 = sum(num == 0 for num in nums2)

        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)

        min_sum1 = nums1_sum + zero_count1
        min_sum2 = nums2_sum + zero_count2

        if min_sum1 == min_sum2:
            return min_sum1
        
        if min_sum1 < min_sum2:
            if zero_count1 == 0:
                return -1 # Can't increase first array!
            return min_sum2
        
        if zero_count2 == 0:
            return -1
        return min_sum1
