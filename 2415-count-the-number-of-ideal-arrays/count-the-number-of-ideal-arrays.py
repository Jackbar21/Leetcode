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
        res = 0
        for x in range(1, maxValue + 1):
            prime_factors = self.get_prime_factors(x) # prime-to-freq dictionary!
            combs = [math.comb(n + e - 1, n - 1) for e in prime_factors.values()]
            if len(combs) == 0:
                # No prime factors, hence ONLY combination is to pick the value 'x' for ALL
                # n elements in the array. This is valid, since x is divisible by x for any x!
                res += 1
            else:
                count = functools.reduce(lambda x, y: x * y, combs) % MOD
                res += count
                res %= MOD
        return res
    
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
