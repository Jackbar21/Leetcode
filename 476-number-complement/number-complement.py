class Solution:
    def findComplement(self, num: int) -> int:
        # Convert num to binary (e.g. 5 --> '0b101')
        bin_num = bin(num)

        # Ignore first two characters (e.g. '0b101' --> '101')
        bin_num = str(bin_num[2:])

        # Flip all the digits (e.g. '101' --> '010')
        flipped_bin_num = ''.join(str(1 - int(digit)) for digit in bin_num)
        
        # Convert binary into decimal (e.g. '010' --> 2)
        return int(flipped_bin_num, 2)
        