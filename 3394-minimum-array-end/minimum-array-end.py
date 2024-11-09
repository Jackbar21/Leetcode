class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bin_x = bin(x)[2:]
        bin_num = bin(n - 1)[2:]

        # Add padding as needed
        # if len(bin_num) > len(bin_x):
        #     bin_x = '0' * (len(bin_num) - len(bin_x)) + bin_x

        x_index = len(bin_x) - 1
        num_index = len(bin_num) - 1
        arr = collections.deque()
        while num_index >= 0:
            # All unset bits in x already taken care of, so
            # add rest of nums in bin_num as needed
            if x_index < 0:
                arr.appendleft(bin_num[num_index])
                num_index -= 1
                continue

            if bin_x[x_index] == '0':
                arr.appendleft(bin_num[num_index])
                num_index -= 1
            else:
                # assert bin_x[x_index] == '1'
                arr.appendleft('1')

            # Loop Invariant
            x_index -= 1

        return x | int(''.join(arr), 2)

# x = 01101100000101 == 6913
# n = 01101100010101
#     ______________
#     01101100000101

# 3 --> 11
# 4 --> 100

# 1 0 1 == 1*2^2 + 0*2^1 + 1*2^0 == 5

# nums = [6913, 6915]

# BITWISE AND:
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1