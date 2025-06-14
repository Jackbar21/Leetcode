class Solution:
    def minMaxDifference(self, num: int) -> int:
        str_num = str(num)

        # To make largest number, look at first most significant digit that is NOT a 9
        # Then, make that digit (and all of its other occurances) becomes 9s
        digit_to_replace = None
        for digit in str_num:
            if digit != "9":
                digit_to_replace = digit
                break
        max_num = num if digit_to_replace is None else int("".join(digit if digit != digit_to_replace else "9" for digit in str_num))

        # To make smallest number, look at most significant digit, and make it a 0
        # alongside all its other occurances.
        digit_to_replace = str_num[0]
        min_num = int("".join(digit if digit != digit_to_replace else "0" for digit in str_num))

        return max_num - min_num
