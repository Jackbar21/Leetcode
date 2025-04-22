class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        HINT FROM THE DISCUSSIONS:

        For any number x, with prime factorization:
            x = p_0^{e_0} * p_1^{e_1} * ... * p_{k - 1}^{e_{k - 1}}

        the number of arrays of length n ending in x is equal to:
            C(n - 1 + e_0, e_0) * C(n - 1 + e_1, e_1) * ... * C(n - 1 + e_{k - 1}, e_{k - 1})
        """

        # Using above hint, we can fix the last value x as any number in range [1, maxValue]
        # and then count the total number of arrays of length n ending in x via above formula!
        MOD = pow(10, 9) + 7

        # Step 1: Use Sieve of Eratosthenes to find all prmie numbers <= maxValue!
        sieve = [True] * (maxValue + 1)
        sieve[0] = sieve[1] = False
        for prime in range(2, maxValue + 1):
            if not sieve[prime]:
                continue
            for non_prime in range(pow(prime, 2), maxValue + 1, prime):
                sieve[non_prime] = False
        primes = [i for i in range(len(sieve)) if sieve[i]]
        self.primes = primes

        # Step 2: Fix x as last value in array for every possible x in range [1, maxValue],
        # and count total number of possible answers for each x via formula in hint above.
        res = []
        for x in range(1, maxValue + 1):
            prime_factors = self.get_prime_factors(x) # prime-to-freq dictionary!
            combs = list(map(lambda e: math.comb(n + e - 1, n - 1), prime_factors.values()))
            if len(combs) == 0:
                # No prime factors, hence can only pick one 'k' and (n-1) '1's, for a total
                # of n possibilities. Unless k == 1, in which case it's just n '1's all together.
                # assert False
                # res.append(n if e != 1 else 1)
                res.append(1)
                print(f"ALERT")
            else:
                val = functools.reduce(lambda x, y: x * y, combs) % MOD
                res.append(val)
        print(f"{res=}")
        return sum(res) % MOD



        # res = 0
        # for start_num in range(1, maxValue + 1):
        #     count = self.dp(n - 1, start_num)
        #     res = (res + count) % MOD
        # return res % MOD
    
    # @cache
    # def dp(self, num_left, cur_num):
    #     MOD = self.MOD
    #     if num_left == 0:
    #         return 1
        
    #     res = 0
    #     # for next_num in range((2 if cur_num == 1 else cur_num ** 2), self.max_value + 1, cur_num):
    #     for next_num in range(cur_num + cur_num, self.max_value + 1, cur_num):
    #         res = (res + self.dp(num_left - 1, next_num)) % MOD
    #     return res % MOD
    
    @cache
    def get_prime_factors(self, n):
        prime_factors = defaultdict(int)
        prime_index = 0
        while n > 1:
            prime = self.primes[prime_index]
            while n % prime == 0:
                n //= prime
                prime_factors[prime] += 1
            
            # Loop Invariant
            prime_index += 1
        
        return prime_factors

