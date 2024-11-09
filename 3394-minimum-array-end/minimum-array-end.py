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
