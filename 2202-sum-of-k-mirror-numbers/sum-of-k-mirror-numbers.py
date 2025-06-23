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
        # queue = collections.deque(["0", "00"])

        # k = 3

        # odd = 101
        # even = 1001
        # processed = [0, 1, 2, 00, 11, 22]

        odd = ["0"]
        even = ["0", "0"]
        max_digit = str(k - 1)
        res = []
        while len(res) < n:
            assert len(odd) % 2 == 1
            assert len(even) % 2 == 0
            assert len(odd) != len(even)
            chose_odd = len(odd) < len(even)
            base_k_num = (odd if chose_odd else even).copy()
            #print(f"base_k_num={''.join(base_k_num)}")
            # base_k_num = [digit for digit in base_k_num]

            # Check if num is valid
            if base_k_num[0] != "0": # No trailing zeros allowed
                base_10_num = int("".join(base_k_num), base=k)
                if self.isPalindrome(base_10_num):
                    res.append(base_10_num)
                    #print(f"ADDED: {res=}")
                    assert len(res) <= n
                    if len(res) == n:
                        #print(f"FINAL(1): {res=}")
                        return sum(res)

            # Update to next num
            next_num = None
            if min(base_k_num) == max_digit:
                next_num = [digit for digit in "1" + "0" * len(base_k_num) + "1"]
            else:
                i = (len(base_k_num) - 1) // 2
                j = len(base_k_num) // 2
                assert base_k_num[i] == base_k_num[j]
                while base_k_num[i] == max_digit:
                    assert base_k_num[i] == base_k_num[j]
                    base_k_num[i] = "0"
                    base_k_num[j] = "0"
                    i -= 1
                    j += 1
                assert base_k_num[i] == base_k_num[j]
                next_digit = str(int(base_k_num[i]) + 1)
                base_k_num[i] = next_digit
                base_k_num[j] = next_digit
                next_num = base_k_num

            
            if chose_odd:
                # assert base_k_num == odd
                #print(f"prev_odd={odd}, new_odd={next_num}")
                odd = next_num
            else:
                # assert base_k_num == even
                #print(f"prev_odd={even}, new_odd={next_num}")
                even = next_num
            
            #print()
                
            

        #print(f"FINAL(2): {res=}")
        return sum(res)