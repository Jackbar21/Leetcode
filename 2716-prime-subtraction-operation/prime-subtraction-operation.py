class Solution:
    def __init__(self):
        self.sieve = None

    def findLargestValidPrime(self, n):
        # Want to find LARGEST prime number p that is STRICTLY less than n
        # We can use the sieve built at beginning of problems as our range
        # of primes to search from

        l, r = 0, len(self.sieve) - 1
        res = 0
        while l <= r:
            mid = (l + r) // 2
            prime = self.sieve[mid]

            if prime < n:
                res = max(res, prime)
                l = mid + 1
            else:
                r = mid - 1
        
        # If no solution, res == 0, which is great since subtracting anything
        # by 0 has absolutely no effect anyways :)
        return res

    def primeSubOperation(self, nums: List[int]) -> bool:
        # Step 1: Build sieve of erastocrenes
        n = max(nums)
        primes = set([i for i in range(2, n + 1)])
        for power in range(2, math.ceil(math.sqrt(n))):
            base = power + power
            while base <= n:
                if base in primes:
                    primes.remove(base)
                base += power
        self.sieve = list(primes)

        # Thanks to Python, set will not lose ordering, so no need to
        # sort the numbers in primes (already the case for you!)
        # assert self.sieve == sorted(self.sieve)

        nums[0] -= self.findLargestValidPrime(nums[0])
        for i in range(1, len(nums)):
            # Want to find LARGEST prime number p such that:
            #   (1) p < nums[i]
            #   (2) nums[i - 1] < nums[i] - p (unless i == 0)
            #       <==> p < nums[i] - nums[i - 1] < nums[i], since nums[i - 1] >= 1
            # So really, ONLY want to find LARGEST prime number p such that:
            #   (1) p < nums[i] - nums[i - 1]
            # Since it's special for i == 0, that case is handled separately first above
            nums[i] -= self.findLargestValidPrime(nums[i] - nums[i - 1])

            # Ensure array is always strictly increasing
            if nums[i - 1] >= nums[i]:
                return False
    
        return True
        