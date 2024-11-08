class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # XOR Properties:
        # X ^ 0 == X
        # X ^ X == 0
        # X ^ Y == Y ^ X

        # want to maximize xor ^ k
        # so want k to be INVERSE IN BITS of xor

        # xor = 1110101010101010101
        #  k =  0001010101010101010
        #       ___________________
        #       1111111111111111111

        xor = 0
        for num in nums:
            xor ^= num
        
        # max_k = 1 << maximumBit
        # best_k = [0] * maximumBit

        answer = []
        for i in range(len(nums) - 1, -1, -1):
            bin_xor = bin(xor)
            length = len(bin_xor) - 2

            num_to_take = min(maximumBit, length)
            padding_len = max(0, maximumBit - num_to_take)

            k = '1' * padding_len + ''.join(
                '0' if c == '1' else '1' for c in bin_xor[-num_to_take:]
            )

            # k = '1' * (max(0, maximumBit - length)) # + ''.join(
                # '1' * (maximumBit - len(bin_xor) + 2),  # padding
                # ('0' if bin_xor[len(bin_xor) - 1 - i] == '1' else '1' for i in range(maximumBit))
            # )

            # k = int(''.join('0' if c == '1' else '1' for c in bin(xor)[-maximumBit:]), 2)
            # k = int(''.join('0' if c == '1' else '1' for c in ('G' * maximumBit + bin(xor))[-maximumBit:]), 2)

            # 1 -> 0
            # 0 -> 1

            k = int(k, 2)
            answer.append(k)

            # "Delete" last number in nums
            xor ^= nums[i]

        return answer
