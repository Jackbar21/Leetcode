class Solution:
    def __init__(self):
        self.candidates = None
        self.memo = {}

    def largestCombination(self, candidates: List[int]) -> int:
        # max_bitwise_and = int('1' * (len(bin(max(candidates))) - 2), 2)
        max_num_bits = len(bin(max(candidates))) - 2
        # self.candidates = candidates
        
        res = 0
        for i in range(max_num_bits):
            bit_index = -i - 1
            # TODO: hash binary representation of each number to see if affects performance
            count = 0
            for num in candidates:
                bin_num = bin(num)
                if -bit_index <= len(bin_num) and bin_num[bit_index] == '1':
                    count += 1
            res = max(res, count)

        return res
        return self.largestCombinationDp(0)
    def largestCombinationDp(self, i, prev_bitwise_and = None):
        # Prevent solutions with non-positive bitwise and
        if i >= len(self.candidates):
            return 0 if prev_bitwise_and is None or prev_bitwise_and > 0 else float('-inf')
        
        if (i, prev_bitwise_and) in self.memo:
            return self.memo[(i, prev_bitwise_and)]
        
        # Case 1: Don't include index i
        case1 = self.largestCombinationDp(i + 1, prev_bitwise_and)

        # Case 2: Include index i
        # Can only do so if bitwise_and remains POSITIVE
        case2 = float('-inf')
        if prev_bitwise_and is None:
            case2 = 1 + self.largestCombinationDp(i + 1, self.candidates[i])
        elif prev_bitwise_and & self.candidates[i] > 0:
            case2 = 1 + self.largestCombinationDp(i + 1, prev_bitwise_and & self.candidates[i])

        res = max(case1, case2)
        # if case2 > case1:
        #     print(self.candidates[i])
        self.memo[(i, prev_bitwise_and)] = res
        return res
        
