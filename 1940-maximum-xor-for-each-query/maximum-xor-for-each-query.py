class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # XOR Properties:
        # X ^ 0 == X
        # X ^ X == 0
        # X ^ Y == Y ^ X

        # Get xor of all numbers in nums
        xor = 0
        for num in nums:
            xor ^= num
        
        # Want to maximize xor ^ k so want k to be INVERSE IN BITS of xor
        # xor = 1110101010101010101
        # k   = 0001010101010101010
        #       ___________________
        #       1111111111111111111

        answer = []
        for i in range(len(nums) - 1, -1, -1):
            bin_xor = bin(xor)
            length = len(bin_xor) - 2

            num_to_take = min(maximumBit, length)
            padding_len = max(0, maximumBit - num_to_take)

            k = int('1' * padding_len + ''.join(
                '0' if c == '1' else '1' for c in bin_xor[-num_to_take:]
            ), 2)
            answer.append(k)

            # Loop Invariant - "Delete" last number in nums
            xor ^= nums[i]

        return answer
