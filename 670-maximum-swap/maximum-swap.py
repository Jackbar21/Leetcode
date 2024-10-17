class Solution:
    def maximumSwap(self, num: int) -> int:
        # str_num = str(num)
        str_num = [digit for digit in str(num)]


        max_suffix = collections.deque([])
        max_digit = float("-inf")
        max_index = -1
        for i in range(len(str_num) - 1, -1, -1):
            digit = int(str_num[i])
            if digit > max_digit:
                max_digit, max_index = digit, i

            # max_digit = max(max_digit, int(str_num[i]))
        
            max_suffix.appendleft((max_digit, max_index))
        
        # print(max_suffix)
        # return 1

        NUM, INDEX = 0, 1
        for i in range(len(str_num)):
            digit = int(str_num[i])
            if digit < max_suffix[i][NUM]:
                print(str_num)
                index = max_suffix[i][INDEX]
                assert i != index
                tmp = str_num[i]
                str_num[i] = str_num[index]
                str_num[index] = tmp

                # str_num[i], str_num[max_suffix[i][INDEX]] = str_num[i], str_num[max_suffix[i][INDEX]]
                print(str_num, i, max_suffix[i][INDEX])
                # return int(''.join(str_num))
                print("DASA")
                break

        return int("".join(str_num))
        # raise Exception("Unreachable Code!")
        
        l = 0
        while l < len(str_num) and str_num[l] == "9":
            l += 1
        if l == len(str_num):
            # All digits are 9, so no need for swap
            return num
        
        # Otherwise, index l is the index of the first non-9
        # if str_num[0] == "9"