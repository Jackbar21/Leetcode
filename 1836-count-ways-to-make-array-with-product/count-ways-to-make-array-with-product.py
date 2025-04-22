class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        max_k = max(k for (n, k) in queries)

        # Sieve of Eratosthenes
        sieve = [True] * (max_k + 1)
        sieve[0] = sieve[1] = False
        for prime in range(2, max_k + 1):
            if not sieve[prime]:
                continue
            for non_prime in range(pow(prime, 2), max_k + 1, prime):
                sieve[non_prime] = False
        
        primes = [i for i in range(len(sieve)) if sieve[i]]
        self.primes = primes

        # return [self.dp(n, k) % MOD for n, k in queries]
        res = []
        for n, k in queries:
            print(f"NEW QUERY:")
            print(f"{n, k=}")
            print(f"{self.get_prime_factors(k)=}")
            print(f"self.query_solver({n}, {k})={self.query_solver(n, k) % MOD}")
            # x = len(self.get_prime_factors(k))
            # res.append(math.comb(x + n - 1, n - 1) % MOD)
            # res.append(
            #     sum(math.perm(n + x - 1, n - 1)
            #     for x in self.get_prime_factors(k).keys()) % MOD
            # )
            prime_factors = self.get_prime_factors(k)
            combs = list(map(lambda x: math.comb(n + x - 1, n - 1), prime_factors.values()))
            if len(combs) == 0:
                # No prime factors, hence can only pick one 'k' and (n-1) '1's, for a total
                # of n possibilities. Unless k == 1, in which case it's just n '1's all together.
                res.append(n if k != 1 else 1)
            else:
                val = functools.reduce(lambda x, y: x * y, combs) % MOD
                res.append(val)
        return res

    
    def query_solver(self, n, k):
        # Case 1: array with k once, and (n-1) 1s. There are n slots to choose k, rest are ones
        case1 = math.comb(n, 1)
        assert case1 == n

        # Case 2: Use ALL the prime factors!
        d = self.get_prime_factors(k)
        # assert k not in d # TODO: might be false
        print(f"{d=}")

        x = len(d)
        return math.comb(x + n - 1, n - 1)

        count_factors = sum(d.values())
        if count_factors > n:
            return False
        
        assert 1 not in d
        if count_factors < n:
            d[1] = n - count_factors # If don't have enough factors, multiply by a bunch of ones!
        print(f"{d=}")
        
        numerator = math.factorial(n)
        denominator = 1
        for freq in d.values():
            denominator *= math.factorial(freq)
        assert numerator % denominator == 0
        case2 = numerator // denominator

        print(f"{n=}, {k=}, {case1=}, {case2=}")
        return case1 + case2

    
    @cache
    def get_prime_factors(self, n):
        prime_factors = defaultdict(int)
        prime_index = 0
        while n > 1:
            prime = self.primes[prime_index]
            # if n % prime == 0:
            #     prime_factors.append(prime)
            #     while (n % prime == 0):
            #         n //= prime
            while n % prime == 0:
                n //= prime
                prime_factors[prime] += 1
            
            # Loop Invariant
            prime_index += 1
        
        return prime_factors
        
        
    
    @cache
    def dp(self, num_left, product_left):
        if num_left == 0:
            return product_left == 1
        
        if product_left < 1:
            return False
        
        # count = self.dp(num_left - 1, product_left)
        count = 0
        # for divisor in range(1, product_left + 1):
        for divisor in self.get_prime_factors(product_left):
            assert product_left % divisor == 0
            count += self.dp(num_left - 1, product_left // divisor)
        return count