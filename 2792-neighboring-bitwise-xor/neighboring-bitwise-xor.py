class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        Let o_i = original[i] for each index in the range [0, n - 1]
        derived = [
            o_0 ^ o_1,
            o_1 ^ o_2,
            o_2 ^ o_3,
            .
            .
            .
            o_{n-1} ^ o_0
        ]

        Which means if we XOR all of the elements together, we should end up with:
        (o_0 ^ o_1) ^ (o_1 ^ o_2) ^ (o_2 ^ o_3) ^ ... ^ (o_{n-1} ^ o_0)
            <==>
        (o_0 ^ o_0) ^ (o_1 ^ o_1) ^ (o_2 ^ o_2) ^ (o_3 ^ o_3) ^ ... ^ (o_{n-1} ^ o_{n-1})
            <==>
        (0) ^ (0) ^ (0) ^ (0) ^ ... ^ (0)
            <==>
        0

        Hence, we should just ensure that XOR'ing all of the elements in the derived array
        results in 0! Otherwise, we know that it could NOT have been derived from a binary
        array's adjacent pairs!
        """
        val = 0
        for bit in derived:
            val ^= bit
        return val == 0
