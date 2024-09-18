class Solution:
    def bigger(self, num_a: str, num_b: str):
        # e.g. num_a == 34, num_b == 30000
        # 3430000 > 3000034
        
        if num_a + num_b > num_b + num_a:
            print(f"{num_a + num_b} > {num_b + num_a} --> {True}")
            return num_a
        
        print(f"{num_a + num_b} > {num_b + num_a} --> {False}")
        return num_b
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums =  self.largestNumberHelper(nums)
        print(f"END: {sorted_nums=}")
        res = ''.join(str(num) for num in sorted_nums)
        if res == "0" * len(res):
            return "0"
        return res
    def largestNumberHelper(self, nums, depth = 0):
        groups = {digit: [] for digit in "0123456789"}
        for num in nums:
            # if num == 0:
            #     zero_count += 1
            #     continue
            group = str(num)[0]
            groups[group].append(str(num))
        
        print(groups)
        # return ""

        sorted_nums = []
        for level in "9876543210":
            sorted_level = self.magicSort(groups[level], level)
            sorted_nums.extend(sorted_level)

        return sorted_nums
        # return ''.join(str(num) for num in sorted_nums)


        # 8999999999999999999999
        # 9

        # 30, 301,
    def getFirstNonLevelDigit(self, num: int, level: str) -> int:
        # RETURNS LEVEL IF ALL DIGITS IN NUM ARE EQUAL TO LEVEL.
        i = 0
        str_num = str(num)
        for digit in str_num:
            if digit != level:
                return (digit, i, len(str_num))
            i += 1

        # If all digits are equal to level, we return level to indicate this
        # to be our "pivot" index
        return (level, i, len(str_num))
    
    def getNonLevelDigits(self, num, level):
        str_num = str(num)
        if str_num == level * len(str_num):
            return [(level, float("-inf"))]
        res = []
        index = 0
        while str_num[index] == level:
            index += 1
        i = index
        print(f"{index=}")
        for digit in str_num[index:]:
            # if digit != level:
            res.append((digit, i))
            i += 1
        
        # if len(res) == 0:
        #     return [(level, i)]
        res.append((level, i))
        return res

        return res
    
    def sortFunc2(self, level, digits):
        res = []
        level = int(level)
        assert len(digits) > 0
        for d in digits:
            digit, i = d
            digit = int(digit)
            # assert digit != level

            # If digit > level, want the index to be as small as possible (e.g. 34 better than 33999)
            # If digit < level, want the index to be as large as possible (e.g. 330 better than 32)
            if digit < level:
                # return (digit, i)
                res.append((-i, digit))
            else:
                res.append((i, digit))
        # res.append((-len(digits),))
        print(f"{res=}")
        return tuple(res)
    # Used for non-pivots
    def sortFunc(self, num, level, first_non_level_digit, i, length):
        digit = int(first_non_level_digit)
        level = int(level)
        assert digit != level

        # If digit > level, want the index to be as small as possible (e.g. 34 better than 33999)
        # If digit < level, want the index to be as large as possible (e.g. 330 better than 32)
        if digit < level:
            # return (digit, i)
            return (-i, digit, -length)
        else:
            return (i, digit, -length)

        # 3333333335, 34
            
    def magicSort(self, arr: List[int], level = 3) -> List[int]:
        # At this point, arr represents a certain "level". To make explanation easier,
        # suppose this is level "3".
        # Any other level larger than 3, i.e. 4-9, we can assume to have already been "cleared".
        # This is because any number with a leading digit greater than 3, should be in front
        # (to the small) of any number whose leading digit is less than or equal to 3, in order
        # to maximize the final number. Therefore, we can assume at this stage, that any other
        # number with a leading digit greater than three has already been "cleared"/"considered"
        # and can be safely assumed to "not exist".

        # Idea: we will take all length 1 digits as our "pivot" (there can be 0, 1, or more than
        # one such digits). They will be placed in the "middle" of our result array.
        # In the "small" side of our result array, will be number whose second digit
        if len(arr) <= 1:
            return arr
        
        mid = len(arr)//2
        print(f"{mid=}, {arr}")
        left, right = arr[:mid], arr[mid:]
        left = self.magicSort(left)
        right = self.magicSort(right)

        

        # Idea: we now have "sorted" versions of left and right. We want to essentially
        # always pick the "better" element from either the beginning of left or right,
        # better meaning that it will yield an overall larger number, therefore the 
        # best we can do for our current level in regards to having highest significant
        # digit values. We do this via our 'better' function, which concatenates two
        # numbers together, to check which ordering of concatenation yields the overall
        # larger number.
        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            bigger = self.bigger(left[l], right[r])
            if bigger == left[l]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        
        assert not ((l < len(left)) and (r < len(right)))
        print(f"SOL1: {res}")
        if l < len(left):
            res.extend(left[l:])
        elif r < len(right):
            res.extend(right[r:])
        print(f"SOL2: {res}")
        
        return res

        # '4',1 > '3', 0
        # '0',1 > '2', 0


        # 3*[4-9]*, 3*, 3[1-2][1-9]*


        # 3, 334, 330, 34, 33, 32
        d = {
            num: self.getFirstNonLevelDigit(str(num), level)
            for num in arr
        }

        # 339
        # 34

        small, middle, big = [], [], []
        small_map, big_map = {}, {}

        for num in arr:
            digits = self.getNonLevelDigits(num, level)
            print(f"{num}: {digits=}")
            LEVEL, INDEX = 0, 1
            first_digit = digits[0]
            if len(digits) == 1 and first_digit[LEVEL] == level:
                middle.append(num)
            elif first_digit[LEVEL] < level:
                small_map[num] = tuple(digits)
                small.append(num)
            else:
                big_map[num] = tuple(digits)
                big.append(num)
            
        # return arr
        if level in "43":
            print(small, middle, big)
            print(small_map)
            print(big_map)
        return (
            sorted(big, key = lambda key: self.sortFunc2(level, big_map[key]))
            + middle
            + sorted(small, key = lambda key: self.sortFunc2(level, small_map[key]))
        )


        small, middle, big = {}, [], {}
        small_nums, big_nums = [], []
        for num in arr:
            num_level, index, length = self.getFirstNonLevelDigit(num, level)
            if num_level < level:
                small[num] = (num_level, index, length)
                # small[num] = (index, num_level)
                # small.append(num)
                small_nums.append(num)
            elif num_level == level:
                middle.append(num)
            else:
                assert num_level > level
                # big.append(num)
                big[num] = (num_level, index, length)
                big_nums.append(num)
        if level in "34":
            print(d)
            print(f"{big=}")
            print(f"{middle=}")
            print(f"{small=}")
        # return arr
        return (
            sorted(big_nums, key = lambda key: self.sortFunc(level, big[key][0], big[key][1], big[key][2]))
            + middle
            + sorted(small_nums, key = lambda key: self.sortFunc(level, small[key][0], small[key][1], small[key][2]))
        )
        # return sorted(small, key=self.)
        if level == "3":
            print(f"{small=}")
            print(f"{middle=}")
            print(f"{big=}")


        return big + middle + small
        
        
        
        # return sorted(arr, key=lambda num: self.getFirstNonLevelDigit(num, level), reverse=True)
        # 33
        # 32999999999999999999
        return arr


# 30, 3, 34
# 34, 334, [3, 33], 330, 32

# 399, 39999

# 3*X, 3*Y
# 334X, N M A M, 33...34Y

# 3...34X, 3...34
# either (1) first one to have bigger number
# else if one too short, the next index of the bigger number better be >= level

# 3...34X, 3...34Y

# 34, 30000

# 333343129
# 33334

# 35




# BIG:      39 >>>>>>> 333333333339
# SMALL:    32 <<<<<<< 333333333330

# Things that matter:
# (1) First Non-Level Digit
# (2) Index of occurrance (Big/Small-Dependant)


# 3, 33 <==> 33, 3 ---> 333
# 3, 334 --> 334-[X_1...X_n]-3 > 3-[X_1...X_n]-334
#            3343 ... 3334
# 3, 32 ---> 332
#       332 > 323
# 330, 32 --->  33032 .. 32330
# 34, 334 ---> 34334 .. 33434

# 34, 30000 --> 3430000 vs 30000034

# 3, 30 --> 330, 303