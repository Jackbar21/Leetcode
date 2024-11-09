class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bin_x = bin(x)[2:]
        bin_num = bin(n - 1)[2:]

        x_index = len(bin_x) - 1
        num_index = len(bin_num) - 1
        arr = collections.deque()
        while num_index >= 0:
            if x_index >= 0 and bin_x[x_index] == '1':
                # Not allowed to modify bit
                arr.appendleft('1')
            else:
                arr.appendleft(bin_num[num_index])
                num_index -= 1

            # Loop Invariant
            x_index -= 1

        return x | int(''.join(arr), 2)

# x = 01101100000101 == 6913
# n = 01101100010101
#     ______________
#     01101100000101

# 3 --> 11
# 412738901273882197308912 --> 0b1010111011001101001111011100100010101000010110011110001011111010011010111110000

# 1 0 1 == 1*2^2 + 0*2^1 + 1*2^0 == 5

# nums = [6913, 6915]

# BITWISE AND:
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1