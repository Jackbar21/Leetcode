class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Needed for DP!
        # prefix_max = []
        # max_num = float("-inf")
        # for num in arr:
        #     max_num = max(max_num, num)
        #     prefix_max.append(max_num)
        
        suffix_min = collections.deque()
        min_num = float("inf")
        for num in reversed(arr): # probably uses yielding, hence efficient!
            min_num = min(min_num, num)
            suffix_min.appendleft(min_num)
        
        # self.prefix_max = prefix_max # Needed for DP!
        self.suffix_min = suffix_min
        # max_splits = self.dp(0, len(arr) - 1)
        # max_chunks = max_splits + 1
        # return max_chunks

        # Greedy approach even better than DP!
        res = 1 # Base case is just array itself as 1 and only chunk!
        cur_max = float("-inf")
        for i in range(len(arr) - 1):
            cur_max = max(cur_max, arr[i])
            if cur_max <= suffix_min[i + 1]:
                res += 1
                cur_max = float("-inf")
        return res
    
    @cache
    def dp(self, i, j):
        res = 0
        for k in range(i, j): # i.e. j NOT inclusive!!!
            if self.prefix_max[k] <= self.suffix_min[k + 1]:
                valid_case = 1 + self.dp(i, k) + self.dp(k + 1, j)
                res = max(res, valid_case)
        
        return res
