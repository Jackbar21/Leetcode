class Solution:
    def reverseBits(self, n: int) -> int:
        # return int(('0'*32 + bin(n)[2:])[-32:][::-1], 2)

        # Step 1: Convert n into binary representation
        bin_n = bin(n)[2:]

        # Step 2: Reverse bits of n
        bin_n = bin_n[::-1]

        # Step 3: Pad with 0s until 32 bits long
        len_padding = 32 - len(bin_n)
        bin_n += '0' * len_padding

        # Step 4: Convert back to int, and return
        return int(bin_n, 2)
        