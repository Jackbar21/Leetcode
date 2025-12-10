class Solution:
    def maxOperations(self, s: str) -> int:
        arr = []
        cur_digit = s[0]
        if cur_digit == "0":
            arr.append(0) # zero 1s at begginning
        count = 0
        for digit in s:
            if digit == cur_digit:
                count += 1
            else:
                arr.append(count)
                cur_digit = digit
                count = 1
        if count > 0:
            arr.append(count)
        print(f"{arr=}")

        res = 0
        i = 0
        while i < len(arr) - 1:
            res += arr[i]
            if i + 2 < len(arr):
                arr[i + 2] += arr[i]
            i += 2
        return res
