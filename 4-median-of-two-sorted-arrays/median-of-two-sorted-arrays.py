class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Set nums1 and nums2 to be smaller and larger arrays in length, respectively
        nums1, nums2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        M, N = len(nums1), len(nums2)
        L = M + N
        half = L // 2

        # Binary search on the number of elements to take FROM nums1 (smaller array!)
        l, r = 0, len(nums1)
        magic_x = None
        while l <= r:
            x = (l + r) // 2
            # print(f"{x=}")
            a_max_left = nums1[x - 1] if x - 1 >= 0 else float("-inf")
            a_min_right = nums1[x] if x < len(nums1) else float("inf")
            b_max_left = nums2[half - x - 1] if half - x - 1 >= 0 else float("-inf")
            b_min_right = nums2[half - x] if half - x < len(nums2) else float("inf")
            
            # print(f"{a_max_left, a_min_right=}")
            # assert a_max_left <= a_min_right
            # print(f"{b_max_left, b_min_right=}")
            # assert b_max_left <= b_min_right
            if a_max_left <= b_min_right and b_max_left <= a_min_right:
                # print(f"VALID SOLUTION")
                magic_x = x
                break
            
            if a_max_left <= b_min_right:
                # assert not (b_max_left <= a_min_right)
                l = x + 1
                continue
            
            # assert not (a_max_left <= b_min_right)
            r = x - 1
            continue

        x = magic_x
        # assert x is not None
        min_right = min(
            nums1[x] if x < len(nums1) else float("inf"),
            nums2[half - x] if half - x < len(nums2) else float("inf")
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
