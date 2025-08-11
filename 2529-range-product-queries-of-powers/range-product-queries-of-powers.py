class GenericSegmentTree:
    def __init__(self, nums, func, identity):
        self.nums = nums
        self.func = func
        self.identity = identity

        N = len(nums)
        self.tree = [identity] * (2 * N)

        for i in range(N):
            self.tree[i + N] = nums[i]
        for i in range(N - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def update(self, i, val):
        N = len(self.nums)
        i += N
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
    
    def rangeQuery(self, l, r):
        N = len(self.nums)
        res = self.identity
        l += N
        r += N
        while l < r:
            if l % 2:
                res = self.func(res, self.tree[l])
                l += 1
            if r % 2:
                r -= 1
                res = self.func(res, self.tree[r])
            l //= 2
            r //= 2
        return res
    
    def getVal(self, i):
        return self.rangeQuery(i, i + 1)
        

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Smallest set of powers of 2 that sum to n is simply the powers of 2
        # from binary representation of n.
        MOD = pow(10, 9) + 7
        binary = bin(n)
        power = 1
        powers = []
        for index in range(len(binary) - 1, -1 + 2, -1):
            if binary[index] == "1":
                powers.append(power)
            power *= 2
        
        # Practice with Segment Trees!
        # tree = GenericSegmentTree(powers, lambda x, y: x * y, 1)
        # return [tree.rangeQuery(l, r + 1) % MOD for l, r in queries]

        prefix_products = [] # Don't have to worry about zeroes, so might as well!
        cur_product = 1
        for power in powers:
            cur_product *= power
            prefix_products.append(cur_product)
        getSubarrayProduct = lambda i, j: prefix_products[j] // (prefix_products[i - 1] if i > 0 else 1)
        return [getSubarrayProduct(l, r) % MOD for l, r in queries]
