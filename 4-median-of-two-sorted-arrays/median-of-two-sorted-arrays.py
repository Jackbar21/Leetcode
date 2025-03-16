class Solution:
    # Final Time Complexity: O(log(min(m, n))) <= O(log(m + n)), as wanted!
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Set nums1 and nums2 to be smaller and larger arrays in length, respectively
        nums1, nums2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        M, N = len(nums1), len(nums2)
        # assert M <= N
        L = M + N
        half = L // 2

        # Binary search on the number of elements to take FROM nums1 (smaller array!)
        l, r = 0, M
        magic_x = None
        while l <= r:
            x = (l + r) // 2
            nums1_max_left = nums1[x - 1] if x - 1 >= 0 else float("-inf")
            nums1_min_right = nums1[x] if x < M else float("inf")
            nums2_max_left = nums2[half - x - 1] if half - x - 1 >= 0 else float("-inf")
            nums2_min_right = nums2[half - x] if half - x < N else float("inf")
            
            if nums1_max_left <= nums2_min_right and nums2_max_left <= nums1_min_right:
                magic_x = x
                break
            
            if nums1_max_left <= nums2_min_right:
                # assert not (nums2_max_left <= nums1_min_right)
                l = x + 1
                continue
            
            # assert not (nums1_max_left <= nums2_min_right)
            r = x - 1
            continue

        # assert magic_x is not None
        x = magic_x
        min_right = min(
            nums1[x] if x < M else float("inf"),
            nums2[half - x] if half - x < N else float("inf")
        )
        # assert min_right != float("inf")
        if L % 2 == 1:
            return min_right

        # Since total merged length is even, need to take average of two median elements
        max_left = max(
            nums1[x - 1] if x - 1 >= 0 else float("-inf"),
            nums2[half - x - 1] if half - x - 1 >= 0 else float("-inf")
        )
        # assert max_left != float("-inf")
        return (min_right + max_left) / 2
