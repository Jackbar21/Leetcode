class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False # 2^x > 0, for any integer x
        
        l, r = 0, math.log(n, 2) + 1
        while l <= r:
            mid = (l + r) // 2
            exp = 2 ** mid

            if exp == n:
                return True
            elif exp < n:
                # Need bigger numbers, so search for larger exponents
                l = mid + 1
            else:
                # Need smaller numbers, so search for smaller exponents
                r = mid - 1
        
        return False
