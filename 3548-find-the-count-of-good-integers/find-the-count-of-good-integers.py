class Solution:
    def is_palindrome(self, string: str) -> bool:
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    def is_k_palindromic(self, str_num: str) -> bool:
        return int(str_num[0]) > 0 and (int(str_num) % self.k == 0) #and self.is_palindrome(str_num)

    def countGoodIntegers(self, n: int, k: int) -> int:
        self.n, self.k = n, k
        # d = defaultdict(int)

        # print(f"{self.is_k_palindromic('515')=}")

        # digits = [str(digit) for digit in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        # self.digits = map(str, range(10))
        # for one_digit in digits:
        #     if one_digit == 0: 
        #         continue

        #     for two_digit in digits:
        #         for three_digit in digits:
        #             for four_digit in digits:
        #                 for five_digit in digits:

        # if n == 1:
        #     return sum(map(self.is_k_palindromic, digits))

        # if n % 2 == 1:
        #     # We can have ANY number as center of num
        #     return 10 * self.countGoodIntegers(n - 1, k)
        
        # assert n % 2 == 0
        # assert 

        self.N = math.ceil(n / 2)
        self.offset = 1 if (n % 2 == 1) else 0 # 1 if odd, else 0 if even!
        assert self.N > 0
        self.arr = []
        self.res = 0
        self.sol = set()

        # 10^6

        # 10**5

        self.sufs = []
        self.pals = []
        def backtrack():
            if len(self.arr) >= self.N:
                assert len(self.arr) == self.N
                str_prefix = "".join(map(str, self.arr))
                palindrome = str_prefix + str_prefix[::-1][self.offset:]
                self.sufs.append(str_prefix)
                self.pals.append(palindrome)

                # palindrome = str_prefix + str_prefix[self.offset:][::-1]
                # print(f"{str_suffix=}")
                # print(f"{palindrome=}")
                if self.is_k_palindromic(palindrome):
                    self.res += 1
                    self.sol.add(palindrome)
                return
            
            for digit in range(10):
                # if len(self.arr) == 0 and digit == 0:
                #     continue
                self.arr.append(digit)
                backtrack()
                self.arr.pop()
        
        # DO NOT allow trailing zeroes!
        # for digit in range(1, 10):
        #     self.arr.append(digit)
        #     backtrack()
        #     self.arr.pop()
        backtrack()

        # print(f"{self.sufs=}")
        # print(f"{self.pals=}")
        # return self.res
        print(f"{self.res=}")
        print(f"{self.sol=}")
        assert self.res == len(self.sol)

        def count_rearrange(freq_dict):
            res = 0

            numerator = self.factorial(sum(freq_dict.values()))
            denominator = 1
            for freq in freq_dict.values():
                assert freq >= 1
                if freq > 1:
                    denominator *= self.factorial(freq)
            assert numerator % denominator == 0
            res += numerator // denominator

            # Subtract solutions that contain leading zeroes!
            # print(f"{freq_dict=}")
            if freq_dict.get(0, 0) > 0:
                print(f"{freq_dict=}")
                # numerator -= 1
                # denominator //= self.factorial(freq_dict[0])
                # denominator *= self.factorial(freq_dict[0] - 1)
                # assert numerator % denominator == 0
                freq_dict[0] -= 1
                # if freq_dict[0] == 0:
                #     del freq_dict[0]

                numerator = self.factorial(sum(freq_dict.values()))
                denominator = 1
                for freq in freq_dict.values():
                    # assert freq >= 1
                    if freq > 1:
                        denominator *= self.factorial(freq)
                assert numerator % denominator == 0
                res -= numerator // denominator

            return res

        visited = set()

        res = 0
        for sol in self.sol:
            d = {}
            for digit in sol:
                digit = int(digit)
                d[digit] = d.get(digit, 0) + 1
            
            tup_d = tuple(d.get(digit, 0) for digit in range(10))
            if tup_d in visited:
                continue
            visited.add(tup_d)
            
            # numerator = self.factorial(len(sol))
            # denominator = 1
            # for freq in d.values():
            #     if freq > 1:
            #         denominator *= self.factorial(freq)
            # assert numerator % denominator == 0
            # res += numerator // denominator
            res += count_rearrange(d)

            # Subtract solutions that contain leading zeroes!
            # Can do this 

        return res

    # @cache
    # def dp(num1 = None, num2 = None, num3 = None, num4 = None, num5 = None):
    #     nums = [num for num in [num1, num2, num3, num4, num5] if num is not None)]

    # @cache
    # def dp(str_suffix: str):
    #     palindrome = str_suffix[(1 if self.is_odd else 0):][::-1] + str_suffix

    @cache
    def factorial(self, n):
        assert n >= 0
        if n <= 1:
            return 1
        
        return n * self.factorial(n - 1)

        



    
    # def dp(self, i, d):
    #     if i >= self.n:
    #         return 1