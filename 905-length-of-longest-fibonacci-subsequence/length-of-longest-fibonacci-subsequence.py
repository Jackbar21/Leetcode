class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Map frequency of each number in arr[i:] for every i
        suffix_freqs = []
        d = {}

        # Since arr is STRICTLY increasing, that means every number in arr is UNIQUE.
        # Hence, we can map each number to its index, and use that whenever we "need"
        # a number in one of our DP calls!
        num_to_index = {}
        for i, num in enumerate(arr):
            assert num not in num_to_index
            num_to_index[num] = i
        self.num_to_index = num_to_index

        N = len(arr)
        self.memo = {}
        self.arr = arr
        res = 0
        for i in range(N):
            for j in range(i + 1, N):
                res = max(res, 2 + self.dp(i, j))
        # return max(2 + self.dp(i, j) for i in range(N) for j in range(i + 1, N))

        return res if res >= 3 else 0

        # print(f"{suffix_freqs=}")

        N = len(arr)
        self.arr = arr
        self.memo = {}
        res = 0
        for i, arr_i in enumerate(arr):
            for j in range(i + 1, N):
                base = arr_i + arr[j]
                chain = self.dp(j + 1, base)
                # if chain > 0 and res < base + 2:
                if res < chain + 2:
                    res = chain + 2
        print(f"{self.memo=}")
        return res if res >= 3 else 0
    
    # @cache
    def dp(self, i, j):
        # assert i < j
        if j >= len(self.arr):
            return 0
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        base = self.arr[i] + self.arr[j]
        index = self.num_to_index.get(base, -1)
        self.memo[i] = 1 + self.dp(j, index) if index > j else 0
        return self.memo[i]
        # if index > j:
        #     return 1 + self.dp(j, index)
        
        # return 0

    
    # @cache
    def dp_old(self, i, base):
        if (i, base) in self.memo:
            return self.memo[(i, base)]

        N = len(self.arr)
        if i >= N:
            return 0
        
        num = self.arr[i]
        case1 = 0 if num != base else 1 + self.dp(i + 1, base + num)
        case2 = self.dp(i + 1, base)

        res = max(case1, case2)
        self.memo[(i, base)] = res
        return res
