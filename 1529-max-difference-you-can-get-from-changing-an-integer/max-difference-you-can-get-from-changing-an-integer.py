class Solution:
    def maxDiff(self, num: int) -> int:
        # To get largest difference between a and b, need to make a as LARGE as possible
        # and b as SMALL as possible.

        str_num = str(num)
        all_digits_same = len(set(str_num)) == 1
        if all_digits_same:
            # Largest number will be bunch of 9s, smallest number will be bunch
            # of 1s (since number CANNOT be zero!)
            return int("8" * len(str_num)) # i.e. 999...9 - 111...1 == 888...8
        
        # Not all digits are the same, so no need to worry about that edge case now!
        
        # Step 1: Find 'a', namely LARGEST possible number
        # We do so by finding first non-9 digit, and converting those into 9s!
        digit_to_replace = next(digit for digit in str_num if digit != "9")
        a = int("".join(digit if digit != digit_to_replace else "9" for digit in str_num))
        print(f"{a=}")

        # Step 2: Find 'b', namely SMALLEST possible number
        # Since we cannot have leading zeroes, we have two possible cases:
        # (1) First digit != 1, so can change that one to 1
        # (2) First digit is 1, in which case find first digit>1 and replace those with 0s [if any]
        b = None
        if str_num[0] != "1":
            digit_to_replace = str_num[0]
            b = int("".join(digit if digit != digit_to_replace else "1" for digit in str_num))
        else:
            digit_to_replace = "0" # changing 0 to 0 does nothing :)
            for digit in str_num:
                if int(digit) > 1:
                    digit_to_replace = digit
                    break
            b = int("".join(digit if digit != digit_to_replace else "0" for digit in str_num))

        print(f"{b=}")

        return a - b
