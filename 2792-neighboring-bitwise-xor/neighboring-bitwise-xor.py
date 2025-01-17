class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        Let o_i = original[i] for each index in the range [0, n - 1]
        derived = [
            o_0 ^ o_1,
            o_1 ^ o_2,
            o_2 ^ o_3,
            o_3 ^ o_4,
            .
            .
            .
            o_{n-1} ^ o_0
        ]

        If n - 1 == 4, then we have:
        derived = [
            o_0 ^ o_1,
            o_1 ^ o_2,
            o_2 ^ o_3,
            o_3 ^ o_4,
            o_4 ^ o_0
        ]

        (1. i=0,i=1):  (o_0 ^ o_1) ^ (o_)
        """
        if len(derived) == 1:
            return derived[0] == 0

        val = derived[0]
        for i in range(1, len(derived) - 1):
            val ^= derived[i]
        
        return val == derived[-1]