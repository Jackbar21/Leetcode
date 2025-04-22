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

        res = []
        for n, k in queries:
            prime_factors = self.get_prime_factors(k)
            combs = list(map(lambda x: math.comb(n + x - 1, n - 1), prime_factors.values()))
            if len(combs) == 0:
                # No prime factors, hence can only pick one 'k' and (n-1) '1's, for a total
                # of n possibilities. Unless k == 1, in which case it's just n '1's all together.
                res.append(n if k != 1 else 1)
            else:
                val = functools.reduce(lambda x, y: (x * y) % MOD, combs) % MOD
                res.append(val)
        return res

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
