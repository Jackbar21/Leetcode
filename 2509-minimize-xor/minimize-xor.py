class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin1, bin2 = bin(num1)[2:], bin(num2)[2:]
        bin1_count, bin2_count = bin1.count('1'), bin2.count('1')
        print(f"{bin1=}, {bin1_count=}")
        print(f"{bin2=}, {bin2_count=}")
        # return -1

        # There are only three possible cases:
        # Case 1: bin1_count == bin2_count, in which case we can return num1
        # since num1 ^ num1 == 0 is minimal!
        if bin1_count == bin2_count:
            return num1
        
        
        
        # Case 2: bin1_count < bin2_count, in which case we just set bin2_count
        # least significant bits as 'set' and use that to xor with num1
        if bin1_count < bin2_count:
            bin_num = [bit for bit in bin1]
            i = len(bin_num) - 1
            bits_left = bin2_count - bin1_count
            while bits_left > 0 and i >= 0:
                if bin_num[i] == "0":
                    bin_num[i] = "1"
                    bits_left -= 1
                i -= 1
            return int("".join("1" for _ in range(bits_left)) + "".join(bin_num), 2)
            # return int('1' * bin2_count, 2)

        # Case 3: bin1_count > bin2_count, in which case we want to pair the
        # bin2_count many bits we can set alongside the MOST significant bits
        # inside of num1, that we we can CANCEL them out (since 1 ^ 1 == 0!)
        bin_num = ["0"] * len(bin1)
        # assert bin1_count > bin2_count
        num_bits = bin2_count
        # index = -1
        # while num_bits > 0:
        #     num_bits -= bin1[index] == "1"
        #     index -= 1
        # index += 1
        i = 0
        while num_bits > 0:
            assert i < len(bin_num)
            if bin1[i] == "1":
                bin_num[i] = "1"
                num_bits -= 1
            i += 1

        return int("".join(bin_num), 2)
        print(f"{bin1[index:], int(bin1[index:], 2)=}")