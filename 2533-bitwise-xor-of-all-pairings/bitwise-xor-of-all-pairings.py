class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Say nums1 = [a1,a2,...,a_n]
        And nums2 = [b1,b2,...,b_m]

        Then nums3 = [
            a1^b1, a1^b2, ..., a1^b_m,
            a2^b1, a2^b2, ..., a2^b_m,
            .
            .
            .,
            a_n^b1, a_n^b2, ..., a_n^b_m
        ]

        Taking the xor of all elements would give us, would make it such that
        ALL of the a1,a2,...,a_n values cancel each other out if m is even, otherwise
        have EXACTLY one of each left if m is odd. 
        Similarly, ALL of the b1,b2,...,b_m values cancel each other out if n is even,
        otherwise have EXACTLY one of each left if n is odd.
        """
        xor = 0
        if len(nums1) % 2 == 1:
            for num in nums2:
                xor ^= num

        if len(nums2) % 2 == 1:
            for num in nums1:
                xor ^= num

        return xor
        