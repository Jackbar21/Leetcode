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
        max_splits = self.dp(0, len(arr) - 1)
        max_chunks = max_splits + 1
        return max_chunks
        return self.greedy(0)
    
    def greedy(i, cur_max = float("-inf")):
        if i >= len(self.nums):
            return 0
    
        if self.prefix_max[i] <= self.suffix_min[i + 1]:
            pass
    
    @cache
    def dp(self, i, j):
        res = 0
        for k in range(i, j): # i.e. j NOT inclusive!!!
            if self.prefix_max[k] <= self.suffix_min[k + 1]:
                valid_case = 1 + self.dp(i, k) + self.dp(k + 1, j)
                res = max(res, valid_case)
                return res
        
        return res
