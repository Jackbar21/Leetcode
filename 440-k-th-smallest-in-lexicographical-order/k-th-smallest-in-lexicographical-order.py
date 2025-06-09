class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        STRING_N = str(n)
        STRING_N_LENGTH = len(STRING_N)
        # In yesterday's problem, we were asked to enumerate numbers from [1, n] in lexicographical
        # order. We did so by treating each number as the root of its own node, with 10 unique roots:
        # the digits 1-9; and applying a pre-order traversal on each.
        # Given number (e.g. 10), we must use the same node analogy and figure out how many children
        # lie under that node, to logarithmically find the k'th lexicographically smallest integer.
        memo = {}
        def getNodeCountOld(num: int) -> int:
            if num in memo:
                return memo[num]
            
            if num > n:
                return 0
            
            res = 1
            for offset in range(10):
                res += getNodeCount(num * 10 + offset)
            
            memo[num] = res
            return res
        
        def getNodeCount(num: int) -> int:
            if num > n:
                print(f"num > n triggered for: {num=}, {n=}")
                return 0
            
            # How many numbers exist whose prefix digits is 'num'
            # and whose value is <= n ? 
            prefix_length = len(str(num))
            n_prefix = int(STRING_N[:prefix_length])
            assert len(str(n_prefix)) == prefix_length
            remaining_length = STRING_N_LENGTH - prefix_length
            assert remaining_length >= 0

            # Step 1: Any number whose # of digits is smaller than n's number of digits
            # is fair game, and can be counted.
            res = 1
            for length in range(1, remaining_length): # DO NOT include remaining_length
                res += pow(10, length)
                # print(f"getNodeCount({num})={res}")
            print(f"base result: {res} | before same length, {remaining_length=}")
            
            # As for numbers whose number of digits is the same as n, we must first
            # check whether num, which WLOG we'll say contains X digits, is larger,
            # smaller, or equal to the number formed by the first X digits of n.

            # Case 1: num > n_prefix, in which case there are no solutions of the same length.
            if num > n_prefix:
                print(f"CASE 1: getNodeCount({num})={res}")
                return res
            
            # Case 2: num < n_prefix, in which case all solutions of same length are fair game.
            if num < n_prefix:
                if remaining_length > 0:
                    res += pow(10, remaining_length)
                print(f"CASE 2: getNodeCount({num})={res}")
                return res

            # Case 3: num == n_prefix, in which case solutions limits are determined by n's suffix.
            # For each index, we can either pick:
            #   (1) a digit smaller than STRING_N[i], in which case all remaining indices are free
            #   (2) STRING_N exactly, in which case we're limited again
            assert num == n_prefix
            n_suffix = STRING_N[len(str(n_prefix)):]
            len_suffix = len(n_suffix)
            for i, str_digit in enumerate(n_suffix):
                digit = int(str_digit)
                remaining_digits = len_suffix - i - 1

                res += digit * pow(10, remaining_digits)
            res += 1 # for the number n itself!
            print(f"CASE 3: getNodeCount({num})={res}")
            return res

            # base = 1
            # for str_digit in n_suffix:
            #     valid_possibilities = int(str_digit) + 1
            #     base *= valid_possibilities
            # print(f"CASE 3: getNodeCount({num})={res + base} | res_before={res}, {base=}")
            # res += base
            # return res




        def getNodeCount2(num: int) -> int: 
            # print(f"getNodeCountOld({num})={getNodeCountOld(num)}")
            if num > n:
                print(f"num > n triggered for: {num=}, {n=}")
                return 0

            # How many numbers exist whose prefix digits is 'num'
            # and whose value is <= n ? 
            prefix = str(num)
            prefix_length = len(prefix)
            n_prefix = STRING_N[:prefix_length]

            if num > int(n_prefix):
                # Since num > int(n_prefix), can only consider numbers up to but
                # NOT including STRING_N_LENGTH in length!
                remaining_length = STRING_N_LENGTH - prefix_length
                print(f"{remaining_length=}, {num=}, {prefix=}, {n=}")
                res = 1
                for length in range(1, remaining_length):
                    res += pow(10, length)
                print(f"getNodeCount({num})={res}")
                return res

            
            print(f"{num=}, {n=}")
            assert num <= int(n_prefix)
            if num < int(n_prefix):
                # Since num < int(n_prefix), this means that any suffix
                # is FAIR GAME for the rest of num. E.g. if num = 123
                # and n = 12567, since 123 < 125, we know that 123XY < 12567 = n
                # regardless of what values we choose for X and Y.
                remaining_length = STRING_N_LENGTH - prefix_length
                print(f"{remaining_length=}, {num=}, {prefix=}, {n=}")
                res = 1
                for length in range(1, remaining_length + 1):
                    res += pow(10, length)
                print(f"getNodeCount({num})={res}")
                return res
            
            # Otherwise, it must be that n shares the exact same prefix as num!
            # Hence, the range of possibilties depends on the remaining digits of n
            remaining_length = STRING_N_LENGTH - prefix_length
            # print(f"{remaining_length=}, {num=}, {prefix=}, {n=}")
            res = 1
            for length in range(1, remaining_length):
                res += pow(10, length)
            # print(f"getNodeCount({num})={res}")

            base = 1
            remaining_length = STRING_N_LENGTH - prefix_length
            print(f"{remaining_length=}, {STRING_N[-remaining_length:]=}")
            for digit in STRING_N[-remaining_length:]:
                possibilties = int(digit) + 1
                base *= possibilties
            res += base
            print(f"getNodeCount({num})={res}")
            return res
            
            # res = 1
            # str_num, str_n = str(num), str(n)
            # if 


        for base_digit in range(1, 10):
            node_count = getNodeCount(base_digit)
            # print(f"{base_digit=}, {node_count=}, {k=}")
            if node_count < k:
                k -= node_count
                continue
            
            # print(f"CHOSEN BASE DIGIT: {base_digit=}, {k=}")
            break
        
        def solver(num, k):
            print(f"solver: {num=}, {k=}")
            assert k >= 1
            if k == 1:
                return num
            
            k -= 1
            num *= 10
            for offset in range(10):
                node_count = getNodeCount(num + offset)
                print(f"{num + offset=}, {node_count=}, {k=}")
                if node_count < k:
                    k -= node_count
                    continue
                
                # print(f"CHOSEN NUM DIGIT: {offset=}, {k=}, {num + offset=}")
                # break
                return solver(num + offset, k)
            
            # raise Exception("Unreachable Code!")


        
        return solver(base_digit, k)
