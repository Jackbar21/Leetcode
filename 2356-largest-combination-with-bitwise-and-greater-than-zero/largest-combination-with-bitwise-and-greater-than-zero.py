class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_num_bits = len(bin(max(candidates))) - 2
        
        res = 0
        for i in range(max_num_bits):
            bit_index = -1 - i

            count = 0
            for num in candidates:
                bin_num = bin(num)
                if -bit_index <= len(bin_num) and bin_num[bit_index] == '1':
                    count += 1

            res = max(res, count)

        return res

