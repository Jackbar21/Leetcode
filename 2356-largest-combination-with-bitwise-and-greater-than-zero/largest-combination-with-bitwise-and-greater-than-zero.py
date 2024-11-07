class Solution:
    def __init__(self):
        self.num_to_bin = {}

    def isBitSet(self, num, bit_index):
        # if num not in self.num_to_bin:
        #     self.num_to_bin[num] = bin(num)
        
        # bin_num = self.num_to_bin[num]
        bin_num = bin(num)
        return -bit_index <= len(bin_num) and bin_num[bit_index] == '1'

    
    def largestCombination(self, candidates: List[int]) -> int:
        max_num_bits = len(bin(max(candidates))) - 2
        
        res = 0
        for i in range(max_num_bits):
            bit_index = -i - 1
            # TODO: hash binary representation of each number to see if affects performance
            count = 0
            for num in candidates:
                # bin_num = bin(num)
                # if -bit_index <= len(bin_num) and bin_num[bit_index] == '1':
                #     count += 1
                count += self.isBitSet(num, bit_index)
    
            res = max(res, count)

        return res
