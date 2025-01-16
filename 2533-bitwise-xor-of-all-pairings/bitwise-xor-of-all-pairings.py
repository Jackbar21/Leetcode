class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # nums3 = [num1 ^ num2 for num1 in nums1 for num2 in nums2]
        # res = 0
        # for num in nums3:
        #     res ^= num
        # return res

        xor = 0
        if len(nums1) % 2 == 1:
            for num in nums2:
                xor ^= num
        if len(nums2) % 2 == 1:
            for num in nums1:
                xor ^= num
        return xor
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

        Taking the xor of all elements would give us:

        """