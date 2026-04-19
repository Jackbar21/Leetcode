class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # Just be greedy
        i = j = 0
        M, N = len(nums1), len(nums2)

        res = 0

        # For every index i, find rightmost index j such that conditions hold
        for i in range(len(nums1)):
            l, r = i, len(nums2) - 1
            j = 0
            while l <= r:
                mid = (l + r) // 2
                assert i <= mid
                if nums1[i] <= nums2[mid]:
                    j = mid
                    l = mid + 1
                else:
                    r = mid - 1
            
            res = max(res, j - i)
        
        return res


        res = 0

        while i < M and j < N:
            print(f"{i=}, {j=}, {i <= j}, {nums1[i] <= nums2[j]}")
            if i > j or nums1[i] > nums2[j]:
                j += 1
                continue
            
            print(f"{res=}, {i=}, {j=}")
            res = max(res, j - i)
            i += 1
        
        return res
