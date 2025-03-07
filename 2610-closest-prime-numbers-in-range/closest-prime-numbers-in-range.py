class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = set(filter(lambda num: num & 1, range(left, right + 1)))
        primes.discard(1) # 1 is NOT a prime number!
        if left <= 2:
            primes.add(2) # 2 IS a prime number!
        base = 3
        
        while base <= math.sqrt(right):
            num = base * base
            while num <= right:
                primes.discard(num)
                num += base
            
            base += 1
        
        ans = [-1, -1]
        cur_diff = float("inf")
        sorted_primes = sorted(primes)
        prev = float("-inf")
        for cur in sorted_primes:
            if cur - prev < cur_diff:
                cur_diff = cur - prev
                ans = [prev, cur]
            
            # Loop Invariant
            prev = cur

        # print(f"{primes=}")
        return ans

