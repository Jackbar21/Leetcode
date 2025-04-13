class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        num_even = math.ceil(n / 2)
        num_odd = n // 2
        EVEN_CHOICES, PRIME_CHOICES = 5, 4
        return (pow(EVEN_CHOICES, num_even, MOD) * pow(PRIME_CHOICES, num_odd, MOD)) % MOD