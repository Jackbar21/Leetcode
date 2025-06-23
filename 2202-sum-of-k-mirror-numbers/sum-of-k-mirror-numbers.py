class Solution:
    def isPalindrome(self, num: int) -> bool:
        str_num = str(num)
        l, r = 0, len(str_num) - 1
        while l < r:
            if str_num[l] != str_num[r]:
                return False
            l += 1
            r -= 1
        return True

    def kMirror(self, k: int, n: int) -> int:
        odd = ["0"]
        even = ["0", "0"]
        max_digit = str(k - 1)
        res = 0
        found = 0
        while True:
            base_k_num = odd if len(odd) < len(even) else even

            # Check if num is valid
            if base_k_num[0] != "0": # No trailing zeros allowed
                base_10_num = int("".join(base_k_num), base=k)
                if self.isPalindrome(base_10_num):
                    res += base_10_num
                    found += 1
                    if found == n:
                        return res

            # Update to next num
            if min(base_k_num) == max_digit:
                base_k_num.extend(["0", "1"])
                base_k_num[0] = "1"
                for i in range(1, len(base_k_num) - 2):
                    base_k_num[i] = "0"
            else:
                i = (len(base_k_num) - 1) // 2
                j = len(base_k_num) // 2
                while base_k_num[i] == max_digit:
                    base_k_num[i] = "0"
                    base_k_num[j] = "0"
                    i -= 1
                    j += 1
                next_digit = str(int(base_k_num[i]) + 1)
                base_k_num[i] = next_digit
                base_k_num[j] = next_digit
            
        raise Exception("Unreachable Code")
