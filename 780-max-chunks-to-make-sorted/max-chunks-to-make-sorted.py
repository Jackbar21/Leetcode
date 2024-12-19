class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prefix_max = []
        max_num = float("-inf")
        for num in arr:
            max_num = max(max_num, num)
            prefix_max.append(max_num)
        
        suffix_min = collections.deque()
        min_num = float("inf")
        for num in reversed(arr): # probably uses yielding == efficient
            min_num = min(min_num, num)
            suffix_min.appendleft(min_num)
        
        # print(f"{prefix_max=}")
        # print(f"{suffix_min=}")
        # return 0
        self.prefix_max = prefix_max
        self.suffix_min = suffix_min
        self.nums = arr
        return self.dp(0, len(arr) - 1) + 1
    
    @cache
    def dp(self, i, j):
        res = 0
        for k in range(i, j): # i.e. j NOT inclusive!!!
            if self.prefix_max[k] <= self.suffix_min[k + 1]:
                valid_case = 1 + self.dp(i, k) + self.dp(k + 1, j)
                res = max(res, valid_case)
        
        return res


        # arr[i..j]

        # arr[i..k], arr[k+1..j]