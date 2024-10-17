class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = [digit for digit in str(num)]
        n = len(str_num)

        max_digit = int(str_num[-1])
        max_index = n - 1
        max_suffix = [(max_digit, max_index)]
        for i in range(n - 2, -1, -1):
            digit = int(str_num[i])
            if digit > max_digit:
                max_digit, max_index = digit, i

            max_suffix.append((max_digit, max_index))

        for i in range(n):
            digit = int(str_num[i])
            number, index = max_suffix[n - 1 - i]
            if digit < number:
                # assert i != index
                tmp = str_num[i]
                str_num[i] = str_num[index]
                str_num[index] = tmp
                break

        return int("".join(str_num))
