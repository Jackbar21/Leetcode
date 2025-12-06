class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = pow(10, 9) + 7

        # A segment tree is a be fantastic to get min/max of subarray in O(logn) time
        max_func = lambda a, b: a if a > b else b
        min_func = lambda a, b: a if a < b else b
        max_tree = GenericSegmentTree(nums, max_func, float("-inf"))
        min_tree = GenericSegmentTree(nums, min_func, float("inf"))
        getSubarrayMin = lambda i, j: min_tree.rangeQuery(i, j + 1)
        getSubarrayMax = lambda i, j: max_tree.rangeQuery(i, j + 1)
        isValidSubarray = lambda i, j: getSubarrayMax(i, j) - getSubarrayMin(i, j) <= k

        # Before, I was using binary search to find rightmost index j (in every dp(i) call) such
        # that nums[i..j] is valid subarray -- via 'isValidSubarray' function above. However,
        # we can use prefix sums in here to remove that O(logn) calculation per dp(i) call
        rightmost = []
        l = 0
        for r in range(N):
            while not isValidSubarray(l, r):
                rightmost.append(r - 1)
                l += 1
        rightmost.extend([N - 1] * (N - l))
        self.rightmost = rightmost
        print(f"{l=}, {r=}, {rightmost=}")



        self.memo = {}
        self.suffix_memo = {}

        self.MOD = MOD
        self.nums = nums
        self.isValidSubarray = isValidSubarray

        return self.dp(0) % MOD
    
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]

        nums = self.nums
        N = len(nums)

        if i >= N:
            return 1
        
        # Find largest index j >= i such that nums[i..j] is valid
        # l, r = i, N - 1
        # largest = l
        # while l <= r:
        #     mid = (l + r) // 2
        #     if self.isValidSubarray(i, mid):
        #         largest = mid
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        largest = self.rightmost[i]

        # res = sum(self.dp(j + 1) for j in range(i, largest + 1))
        # Above line of code is too slow, so we can use dp prefix sums
        # to help us out!
        res = self.dp_subarray_sum(i + 1, largest + 1) % self.MOD
        self.memo[i] = res
        return res 
    
    def dp_suffix(self, i):
        # Returns dp(i) + dp(i+1) + ... + dp(N)
        if i > len(self.nums):
            return 0
        if i in self.suffix_memo:
            return self.suffix_memo[i]

        res = (self.dp(i) + self.dp_suffix(i + 1)) % self.MOD
        self.suffix_memo[i] = res
        return res
    
    def dp_subarray_sum(self, i, j):
        # sum(i..j) == sum(i..N) - sum(j+1..N)
        return (self.dp_suffix(i) - self.dp_suffix(j + 1)) % self.MOD


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