class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # Just be greedy
        M, N = len(nums1), len(nums2)
        res = 0

        # For every index i, find rightmost index j such that conditions hold
        for i in range(M):
            l, r = i, N - 1
            while l <= r:
                mid = (l + r) // 2
                if nums1[i] <= nums2[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            if res < r - i:
                res = r - i
        
        return res
