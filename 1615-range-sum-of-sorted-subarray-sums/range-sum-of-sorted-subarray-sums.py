class Solution:
    def __init__(self):
        self.subarray_sums = []
        self.n = None
        self.nums = None
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        magic_modulo_num = (10 ** 9) + 7
        self.n, self.nums = n, nums

        for level in range(1, n + 1):
            self.populateSubarraySums(level)
        self.subarray_sums.sort()

        res = 0
        for i in range(left - 1, right):
            res += self.subarray_sums[i]
            # res %= magic_modulo_num
        return res % magic_modulo_num

    def populateSubarraySums(self, level):
        n = self.n
        if level > n:
            return
        
        if level == n:
            return self.subarray_sums.append(sum(self.nums))

        # Setup first subarray of length level sum
        cur_sum = 0
        for i in range(level):
            cur_sum += self.nums[i]
        self.subarray_sums.append(cur_sum)

        for i in range(n - level):
            cur_sum -= self.nums[i]
            cur_sum += self.nums[i + level]
            self.subarray_sums.append(cur_sum)
        
        return