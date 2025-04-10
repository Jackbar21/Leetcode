class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        self.start, self.finish, self.limit, self.s = start, finish, limit, s
        finish_count = self.dp(finish) 
        print(f"{finish_count=}")
        start_count = self.dp(start - 1)
        # finish_count = self.count_le(finish)
        # start_count = self.count_le(start - 1)
        
        print(f"{start_count=}")
        return finish_count - start_count
    
    # @cache
    def dp(self, num):
        start, finish, limit, s = self.start, self.finish, self.limit, self.s

        num_string = str(num)
        if len(num_string) < len(s):
            return 0
        
        if len(num_string) == len(s):
            return num >= int(s)

        num_prefix = num_string[:-len(s)]
        assert len(num_prefix) > 0

        num_suffix = num_string[-len(s):]
        assert len(num_suffix) > 0

        # if int(num_suffix) < int(s):
        #     if int(num_prefix) == 0:
        #         return 0
        #     print(f"CHANGING NUM FROM {num} TO {f'{int(num_prefix) - 1}{s}'}")
        #     return self.dp(int(f"{int(num_prefix) - 1}{s}"))
        
        # res = functools.reduce(lambda x, y: x * y, [
        #     min(int(digit), limit) + (i > 0)
        #     for i, digit in enumerate(num_prefix)
        # ])
        res = 0
        exceeded_cap = False
        for i, digit in enumerate(num_prefix):
            digit = int(digit)
            if digit > limit:
                exceeded_cap = True
            if exceeded_cap:
                res += (limit + 1) ** (len(num_prefix) - i)
                return res
            
            res += digit * ((limit + 1) ** (len(num_prefix) - i - 1))
        return res + (int(num_suffix) >= int(s))
            

        # res = 1
        # for i in range(len(num_prefix)):
        #     res 
        
        print(f"{res=}")
        
        # recursive_num = int(('9' * (len(num_prefix) - 1)) + num_suffix)
        # recursive_res = self.dp(int('9' * (len(num_string) - 1)))
        # recursive_res = self.dp(recursive_num)
        recursive_res = 1 if len(num_prefix) > 0 else 0
        for length in range(1, len(num_prefix)):
            recursive_res += limit * ((limit + 1) ** (length - 1))
        print(f"{recursive_res=}")

        full_res = res + recursive_res
        print(f"{full_res=}")
        return full_res

    
    @cache
    def count_le(self, num):
        print(f"count_le({num})")
        start, finish, limit, s = self.start, self.finish, self.limit, self.s

        num_string = str(num)
        if len(num_string) < len(s):
            return 0
        
        if len(num_string) == len(s):
            return num >= int(s)
        
        suffix_string = num_string[-len(s):]
        if int(suffix_string) < int(s):
            prefix_num = int(num_string[:-len(s)])
            if prefix_num == 0:
                return 0
            num_string = f"{prefix_num - 1}{s}"
            print(f"CHANGING NUM FROM {num} TO {num_string}")
            return self.count_le(int(num_string))
        
        prefix_string = num_string[:-len(s)]
        assert len(prefix_string) > 0
        
        res = 1
        for i in range(len(prefix_string)):
            digit = int(prefix_string[i])
            res *= min(digit, limit) + 1
        
        length = len(prefix_string) - 1
        if length > 0:
            res += self.count_le(int(('9' * (length + len(s)))))
        
        # for length in range(1, len(prefix_string)):
        #     res += limit * ((limit + 1) ** (length - 1))
        
        return res

    @cache
    def dp_old(self, num):
        start, finish, limit, s = self.start, self.finish, self.limit, self.s

        num_string = str(num)
        if len(num_string) < len(s):
            return 0
        
        if len(num_string) == len(s):
            return num >= int(s)
        
        # first_digit_possibilities = len(range(0, min(int(num_string[0]), limit) + 1))
        # first_digit_possibilities = len(range(0, min(int(num_string[0]), limit) + 1))
        # # if first_digit_possibilities == 0:
        # #     return 0
        # return first_digit_possibilities * max(1, self.dp(int(num_string[1:])))

        num_suffix = num_string[-len(s):]
        # if int(num_suffix) < int(s):
        add_one = int(num_suffix) >= int(s)
        num_prefix = num_string[:-len(s)]
        if int(num_prefix) == 0:
            return add_one
        
        num = f"{int(num_prefix) - 1}{'9' * len(s)}"
        return add_one + self.dp(int(num))
        
        # first_digit = num_string[0]


    
    def count(self, num):
        # Return count of valid integers 'val' in range [0, num] such that:
        # (1) All digits of val are <= limit
        # (2) Suffix of val is s
        limit, s = self.limit, self.s

        num_string = str(num)
        res = 0
        for prefix_length in range(len(num_string) - len(s) + 1):
            if prefix_length == 0:
                print(f"{prefix_length=}, count={1}")
                res += 1 # Actual number itself!
                continue
            
            count = limit * ((limit + 1) ** (prefix_length - 1)) # No leading zeroes!
            print(f"{prefix_length=}, {count=}")
            res += count
        
        # Now subtract everything whose length is len(num_string) but whose value is GREATER THAN num
        res -= self.handle_greater(num)
        return res
    
    def handle_greater(self, num):
        limit, s = self.limit, self.s

        num_string = str(num)
        prefix_length = len(num_string) - len(s)
        if prefix_length < 0:
            return 0
        
        if prefix_length == 0:
            # If num < s, then can indeed get UP to s and that's it!
            assert len(num_string) == len(s)
            return num < int(s)
        
        suffix_num = int(num_string[-len(s):])
        if suffix_num > int(s):
            prefix_num = num_string[:-len(s)]




    # STEP1: Solve for interim lengths, i.e. every VALID num whose length is len(start) <= k <= len(finish)
    # STEP2: Then SUBTRACT every VALID num whose length is len(start) but is LESS THAN start (num < start).
    # STEP3: Then SUBTRACT every VALID num whose length is len(finish) but is GREATER THAN finish (num > finish).
    # ***OR***
    # STEP1: Solve for interim lengths, i.e. every integer whose length k is len(start) < k < len(finish)
    # STEP2: Then ADD everything whose length is len(start) but is GREATER THAN OR EQUAL TO start.
    # STEP3: Then ADD everything whose length is len(finish) but is LESS THAN OR EQUAL TO finish.
    def solver(self, start, finish, limit, s):
        print(f"{start=}, {finish=}, {limit=}, {s=}")
        start_string, finish_string = str(start), str(finish)
        s_int = int(s)

        res = 0

        # STEP 1: 
        # Solve for interim lengths, i.e. every integer whose length k is len(start) <= k <= len(finish)
        print(f"Start Length: {len(start_string)}")
        print(f"Finish Length: {len(finish_string)}")
        for length in range(len(start_string), len(finish_string) + 1):
            prefix_length = length - len(s)
            if prefix_length <= 0:
                print(f"{length=}, permutations={int(prefix_length == 0)}")
                res += prefix_length == 0 # num equals exact prefix!
                continue

            permutations = limit * ((limit + 1) ** (prefix_length - 1))
            print(f"{prefix_length=}, {permutations=}, {limit=}, {length=}")
            res += permutations
            print(f"{length=}, {permutations=}")
        print(f"Initial (overestimate) result: {res}")
        # return res # OVERESTIMATE

        # STEP 2: 
        # Let's subtract everything whose length is len(start) but is LESS THAN start!
        # if len(start_string) >= len(s):
        #     # First, check the suffix of start_string. If it is larger than s, we must
        #     # carry on and increment the len(s)'th least significant digit.
        #     start_prefix = start_string[:-len(s)]
        #     if any(int(digit) < 9 for digit in start_prefix):
        #         # Cannot increment if all digits in prefix are 9s, as would otherwise move
        #         # on to the NEXT length!
        step2 = self.handle_start(start, limit, s)
        print(f"{step2=}, i.e. numbers whose length is {len(str(start)) - len(s)} but whose value is < {str(start)[:-len(s)]}")
        # min_num = ['0'] * (len(str(start)) - len(s))
        # step2 = 0
        # if len(min_num) > 0:
        #     min_num[0] = '1'
        #     min_num = int(''.join(min_num))
        #     step2 = int(str(start)[:-len(s)]) - min_num + 1
        #     print(f"real step2={step2}")

        step3 = self.handle_finish(finish, limit, s)
        print(f"{step3=}, i.e. numbers whose length is {len(str(finish)) - len(s)} but whose value is > {str(finish)[:-len(s)]}")
        # step3 = 0
        # if (len(str(finish)) - len(s)) > 0:
        #     max_num = int('9' * (len(str(finish)) - len(s)))
        #     step3 = max_num - int(str(finish)[:-len(s)]) + 1
        #     print(f"real step3={step3}")

        # step2 = self.handle_finish(start, limit, s)
        # step3 = self.handle_start(finish, limit, s)
        return res - max(0, step2) - max(0, step3)
    
    def handle_start(self, start, limit, s):
        # Return count of VALID numbers whose length is len(start) but whose values are LESS than start!
        if len(str(start)) != len(str(start - 1)):
            print(f"WOAH START!!!")
            assert len(str(start)) == len(str(start - 1)) + 1
            return 0
        start_string = str(start - 1)
        s_int = int(s)

        res = 0

        
        if len(start_string) < len(s):
            return 0
        
        start_prefix = start_string[:-len(s)]
        start_suffix = start_string[-len(s):]
        
        # First, check the suffix of start_string. If it is SMALLER than s, we must
        # carry on and DECREMENT the len(s)'th least significant digit.
        if int(start_suffix) < s_int:
            # Can ONLY increment if NOT all digits in prefix are 0s, as would otherwise move
            # on to the PREVIOUS length!
            if int(start_prefix) == 0:
                return 0
            new_start = f"{int(start_prefix) - 1}{'9' * len(s)}"
            print(f"CHANGING START FROM: {start} TO {new_start}")
            start = new_start
        
        # prefix_length = len(finish) - len(s)
        assert len(start_string) - len(s) > 0 
        assert len(start_string) - len(s) == len(start_prefix)

        # For each index i in start_prefix, we can choose a digit
        # value k such that int(finish_prefix[i]) <= k <= limit,
        # for a total of limit of range(int(finish_prefix[i]), limit + 1)
        # == (limit + 1) - int(finish_prefix[i]) == limit - int(finish_prefix[i]) + 1
        # for i in range(len(start_prefix)):
        #     assert range(int(start_prefix[i]), limit + 1) == limit - int(start_prefix[i]) + 1
        #     possibilites == limit - int(start_prefix[i]) + 1
        #     res += possibilities
        
        start_prefix = str(start)[:-len(s)]
        print(f"{start_prefix=}")
        # return int("".join([str(min(int(start_prefix[i]), limit)) for i in range(len(start_prefix))]))
        # possibilities = [(limit - int(start_prefix[i]) + 1) for i in range(len(start_prefix))]
        possibilities = [len(range(0, min(int(start_prefix[i]), limit) + 1)) for i in range(len(start_prefix))]
        print(f"pre-possibilities={possibilities}")
        possibilities[0] = max(0, possibilities[0] - 1)
        print(f"start_possibilities={possibilities}")
        res = functools.reduce(lambda x, y: x * y, possibilities)
        return res
    
    def handle_finish(self, finish, limit, s):
        # Return count of numbers whose length is len(finish) but is GREATER THAN finish.
        # This is same as count number whose length is len(finish), and then subtract
        # however many are LESS THAN OR EQUAL TO finish
        less_than_or_equal_to_finish = self.handle_start(finish + 1, limit, s)
        print(f"{less_than_or_equal_to_finish=}")
        prefix_length = len(str(finish)) - len(s)
        print(f"dsa: {prefix_length=}")
        if prefix_length <= 0:
            return (prefix_length == 0) - less_than_or_equal_to_finish
        
        return limit * (limit**(prefix_length-1)) - less_than_or_equal_to_finish


        if len(str(finish)) != len(str(finish + 1)):
            print(f"WOAH FINISH!!!")
            assert len(str(finish)) == len(str(finish + 1)) - 1
            return 0
        finish_string = str(finish + 1)
        s_int = int(s)

        res = 0

        if len(finish_string) < len(s):
            return 0
        
        finish_prefix = finish_string[:-len(s)]
        finish_suffix = finish_string[-len(s):]
        
        # First, check the suffix of finish_string. If it is GREATER than s, we must
        # carry on and INCREMENT the len(s)'th least significant digit.
        if int(finish_suffix) > s_int:
            # Can ONLY increment if NOT all digits in prefix are 9s, as would otherwise move
            # on to the NEXT length!
            if all(int(digit) == 9 for digit in finish_prefix):
                return 0
            new_finish = f"{int(finish_prefix) + 1}{'0' * len(s)}"
            print(f"CHANGING START FROM: {finish} TO {new_finish}")
            finish = new_finish
        
        # prefix_length = len(finish) - len(s)
        assert len(finish_string) - len(s) > 0 
        assert len(finish_string) - len(s) == len(finish_prefix)

        # For each index i in finish_prefix, we can choose a digit
        # value k such that int(finish_prefix[i]) <= k <= limit,
        # for a total of limit of range(int(finish_prefix[i]), limit + 1)
        # == (limit + 1) - int(finish_prefix[i]) == limit - int(finish_prefix[i]) + 1
        # for i in range(len(finish_prefix)):
        #     assert range(int(finish_prefix[i]), limit + 1) == limit - int(finish_prefix[i]) + 1
        #     possibilites == limit - int(finish_prefix[i]) + 1
        #     res += possibilities
        
        finish_prefix = str(finish)[:-len(s)]
        print(f"{finish_prefix=}")
        # possibilities = [(limit - int(finish_prefix[i]) + 1) for i in range(len(finish_prefix))]
        possibilities = [len(range(int(finish_prefix[i]), limit + 1)) for i in range(len(finish_prefix))]
        print(f"pre-possibilities={possibilities}")
        # possibilities[0] = max(0, possibilities[0] - 1)
        finish_possibilities=possibilities
        print(f"{finish_possibilities=}")
        res = functools.reduce(lambda x, y: x * y, possibilities)
        return res






    def numberOfPowerfulInt_old(self, start: int, finish: int, limit: int, s: str) -> int:
        return self.solver(start, finish, limit, s)
        """
    #     print(f"{self.helper(finish, limit, s)=}")
    #     print(f"{self.helper(max(start, int(s)) - 1, limit, s)}")
    #     return (
    #         self.helper(finish, limit, s)
    #         - self.helper(max(start, int(s)) - 1, limit, s)
    #     )
    
    # def helper(self, finish, limit, s):
        # start = float("-inf")
        # We're told from constraints that all characters of s are already <= limit
        assert all(int(digit) <= limit for digit in s)

        # int_s = int(s)
        # if finish <= 
        S_INT = int(s)
        if start < S_INT:
            start = S_INT
        
        if len(str(start)) < len(s):
            start = S_INT
        
        if not (start <= finish):
            return 0
        
        print(f"{start=}")
        res = 0
        if len(str(start)) == len(str(finish)):
            start_prefix = str(start)[:-len(s)]
            finish_prefix = str(finish)[:-len(s)]

            assert len(start_prefix) == len(finish_prefix)
            if len(start_prefix) == 0:
                return str(start).endswith(s) and str(finish).endswith(s)

            pos_to_count = {}
            for pos in range(len(start_prefix)):
                valid_range = range(
                    int(start_prefix[pos]),
                    min(limit, int(finish_prefix[pos]))
                )
                pos_to_count[pos] = len(valid_range)
            print(f"{pos_to_count=}")
            
            # for length in range(1, len(str(finish)) - len(s) + 1):
            for i in range(1):
                # length = len(str(finish)) - len(s)
                length = len(start_prefix)
                print(f"{length=}")
                # ALL numbers whose length as a string is equal to 'length' are FAIR GAME.
                # Hence, the number of LEADING digits will be length - len(s). For each
                # such prefix digit, it must be less than or equal to limit, except for
                # the first one which must additionally be greater than 0 (no leading zeroes!)
                # Then we take number of possibilities per digit, multiply that, and that's the
                # number of LEGAL prefixes
                permutations = max(0, pos_to_count[0] - 1)
                for pos in range(1, length):
                    permutations *= pos_to_count[pos]
                # prefix_length = length - len(s)
                # assert prefix_length > 0
                # permutations = limit * ((limit + 1) ** (prefix_length - 1))
                # print(f"{prefix_length=}, {permutations=}, {limit=}, {length=}")
                res += permutations
            return res
            
        
        print(f"{start=}, {finish=}")

        min_length = len(str(start))
        print(f"{s=}, {start=}, {finish=}")
        assert len(s) <= min_length
        res = 0

        print(f"IMPORTANT: {len(s)=}, {min_length=}")
        if len(s) == min_length:
            res = 1 if S_INT >= start else 0
            min_length += 1
        else:
            ### START ###
            # finish_string = str(finish)
            # finish_suffix = finish_string[-len(s):]
            # print(f"{finish_string=}, {finish_suffix=}, {S_INT=}")
            # if int(finish_suffix) < S_INT:
            #     assert int(finish_string[0]) > 0 # IF NOT TRUE, PROBLEM
            #     if int(finish_string[0]) > 1:
            #         finish = f"{int(finish_string[0]) - 1}{'9' * (len(finish_string) - 1)}"
            #     else:
            #         # finish = f"{'9' * (len(finish_string) - 1)}"
            #         return res # DON'T GO DOWN A DEGREE, ELSE YOU WILL DOUBLE COUNT!!!
            
            is_done = False
            start_string = str(start)
            start_suffix = start_string[-len(s):]
            print(f"{start_string=}, {start_suffix=}, {S_INT=}")
            print(f"{int(start_string[0])=}")
            print(f"{int(start_suffix) > S_INT=}, {int(start_suffix)=}, {S_INT=}")
            if int(start_suffix) > S_INT:
                # assert int(start_string[0]) > 0 # IF NOT TRUE, PROBLEM
                # if int(start_string[0]) < 9:
                #     print("LALALALALLAA")
                #     start = f"{int(start_string[0]) + 1}{'0' * (len(start_string) - 1)}"
                # else:
                #     # finish = f"{'9' * (len(finish_string) - 1)}"
                #     # return res # DON'T GO DOWN A DEGREE, ELSE YOU WILL DOUBLE COUNT!!!
                #     min_length = len(s) + 1
                #     is_done = True
                
                start_prefix = start_string[:-len(s)]
                assert int(start_prefix) > 0
                if int(start_prefix) == '9' * len(start_prefix):
                    min_length = len(s) + 1
                    is_done = True
                else:
                    # finish = f"{int(finish_prefix) - 1}{'9' * len(s)}"
                    start = f"{int(start_prefix) + 1}{'0' * len(s)}"
            
            print(f"PRE-DONE: {start=}")
            if not is_done:
                # FIRST, LET'S TRY SOMETHING SIMPLER
                # pos_to_limit = {}
                pos_to_count = {}
                for pos in range(len(str(start)) - len(s) + 1):
                    # lim = min(limit, int(str(finish)[pos]))
                    count = len(range(int(str(start)[pos]), limit + 1))
                    pos_to_count[pos] = count
                print(f"{start=}, {len(str(start)) - len(s) + 1=}")
                print(f"{pos_to_count=}")
            
                # for length in range(1, len(str(finish)) - len(s) + 1):
                for i in range(1):
                    length = len(str(start)) - len(s)
                    print(f"{length=}")
                    # ALL numbers whose length as a string is equal to 'length' are FAIR GAME.
                    # Hence, the number of LEADING digits will be length - len(s). For each
                    # such prefix digit, it must be less than or equal to limit, except for
                    # the first one which must additionally be greater than 0 (no leading zeroes!)
                    # Then we take number of possibilities per digit, multiply that, and that's the
                    # number of LEGAL prefixes
                    permutations = max(0, pos_to_count[0] - 1)
                    for pos in range(1, length):
                        permutations *= pos_to_count[pos]
                    # prefix_length = length - len(s)
                    # assert prefix_length > 0
                    # permutations = limit * ((limit + 1) ** (prefix_length - 1))
                    # print(f"{prefix_length=}, {permutations=}, {limit=}, {length=}")
                    res += permutations

                # return res
                
                # return res
                print(f"NEW RES: {res=}")
                min_length = len(s) + 1

            ### END ###

        
        ### CONTINUE ###

        max_length = len(str(finish))
        max_length -= 1 # Handle at the end!
        # assert min_length <= max_length # TODO: might not be true, off by one?

        print(f"{list(range(min_length, max_length + 1))=}")
        for length in range(min_length, max_length + 1):
            # ALL numbers whose length as a string is equal to 'length' are FAIR GAME.
            # Hence, the number of LEADING digits will be length - len(s). For each
            # such prefix digit, it must be less than or equal to limit, except for
            # the first one which must additionally be greater than 0 (no leading zeroes!)
            # Then we take number of possibilities per digit, multiply that, and that's the
            # number of LEGAL prefixes
            prefix_length = length - len(s)
            assert prefix_length > 0
            permutations = limit * ((limit + 1) ** (prefix_length - 1))
            print(f"{prefix_length=}, {permutations=}, {limit=}, {length=}")
            res += permutations
        
        print(f"{res=}")
        # return res # EXPECT THIS TO BE ***UNDERESTIMATE***

        # All that's left now, is to compute number of permutations regarding total number of digits
        # in len(str(finish))! However, we CANNOT surpass the value of finish!


        # # FIRST, LET'S TRY SOMETHING SIMPLER
        # pos_to_limit = {}
        # for pos in range(len(str(finish)) - len(s)):
        #     lim = min(limit, int(str(finish)[pos]))
        #     pos_to_limit[pos] = lim
        
        # for length in range(1, len(str(finish)) - len(s) + 1):
        #     # ALL numbers whose length as a string is equal to 'length' are FAIR GAME.
        #     # Hence, the number of LEADING digits will be length - len(s). For each
        #     # such prefix digit, it must be less than or equal to limit, except for
        #     # the first one which must additionally be greater than 0 (no leading zeroes!)
        #     # Then we take number of possibilities per digit, multiply that, and that's the
        #     # number of LEGAL prefixes
        #     permutations = 1
        #     for pos in range(length):
        #         permutations *= pos_to_limit[pos] + 1
        #     # prefix_length = length - len(s)
        #     # assert prefix_length > 0
        #     # permutations = limit * ((limit + 1) ** (prefix_length - 1))
        #     # print(f"{prefix_length=}, {permutations=}, {limit=}, {length=}")
        #     res += permutations

        # return res

        finish_string = str(finish)
        finish_suffix = finish_string[-len(s):]
        print(f"{finish_string=}, {finish_suffix=}, {S_INT=}")
        if int(finish_suffix) < S_INT:
            # assert int(finish_string[0]) > 0 # IF NOT TRUE, PROBLEM
            # if int(finish_string[0]) > 1:
            #     finish = f"{int(finish_string[0]) - 1}{'9' * (len(finish_string) - 1)}"
            # else:
            #     # finish = f"{'9' * (len(finish_string) - 1)}"
            #     return res # DON'T GO DOWN A DEGREE, ELSE YOU WILL DOUBLE COUNT!!!
            
            finish_prefix = finish_string[:-len(s)]
            assert int(finish_prefix) > 0
            if int(finish_prefix) == 1:
                return res
            else:
                finish = f"{int(finish_prefix) - 1}{'9' * len(s)}"

        print(f"{finish=}")

        # FIRST, LET'S TRY SOMETHING SIMPLER
        pos_to_limit = {}
        for pos in range(len(str(finish)) - len(s) + 1):
            lim = min(limit, int(str(finish)[pos]))
            pos_to_limit[pos] = lim
        print(f"{pos_to_limit=}")
        
        # for length in range(1, len(str(finish)) - len(s) + 1):
        for i in range(1):
            length = len(str(finish)) - len(s)
            print(f"{length=}")
            # ALL numbers whose length as a string is equal to 'length' are FAIR GAME.
            # Hence, the number of LEADING digits will be length - len(s). For each
            # such prefix digit, it must be less than or equal to limit, except for
            # the first one which must additionally be greater than 0 (no leading zeroes!)
            # Then we take number of possibilities per digit, multiply that, and that's the
            # number of LEGAL prefixes
            permutations = pos_to_limit[0]
            for pos in range(1, length):
                permutations *= pos_to_limit[pos] + 1
            # prefix_length = length - len(s)
            # assert prefix_length > 0
            # permutations = limit * ((limit + 1) ** (prefix_length - 1))
            # print(f"{prefix_length=}, {permutations=}, {limit=}, {length=}")
            res += permutations

        return res


# start = 1829505, finish = 1255574165
"""