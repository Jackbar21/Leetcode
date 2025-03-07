class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        ### FROM WIKIPEDIA (START) ###
        """
        algorithm Sieve of Eratosthenes is
        input: an integer n > 1.
            output: all prime numbers from 2 through n.

            let A be an array of Boolean values, indexed by integers 2 to n,
            initially all set to true.

            for i = 2, 3, 4, ..., not exceeding √n do
                if A[i] is true
                    for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n do
                        set A[j] := false

            return all i such that A[i] is true.
        """
        ### FROM WIKIPEDIA (END) ###

        ### SOLUTION USING WIKIPEDIA PSEUDOCODE AS INSPIRATION: ###
        A = [True] * (right + 1)
        i = 2
        MAX = math.sqrt(right)
        while i <= MAX:
            if A[i]:
                j = i * i
                while j <= right:
                    A[j] = False
                    j += i

            # Loop Invariant
            i += 1
        
        ans = [-1, -1]
        cur_diff = float("inf")
        sorted_primes = [i for i in range(left + (left == 1), right + 1) if A[i]]
        prev = float("-inf")
        for cur in sorted_primes:
            if cur - prev < cur_diff:
                cur_diff = cur - prev
                ans = [prev, cur]
            
            # Loop Invariant
            prev = cur

        # print(f"{primes=}")
        return ans




        ### WORKING SOLUTION (SLOW) WITHOUT USING ANY EXTERNAL RESOURCES: ###
        primes = set(range(left + (left % 2 == 0), right + 1, 2))
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

