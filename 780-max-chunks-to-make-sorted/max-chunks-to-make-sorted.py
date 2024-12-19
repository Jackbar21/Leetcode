class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        suffix_min = collections.deque() # suffix_min[i] == min(arr[i..n-1]), n == len(arr)
        min_num = float("inf")
        for num in reversed(arr): # probably uses yielding, hence efficient!
            min_num = min(min_num, num)
            suffix_min.appendleft(min_num)
        
        # 1 initially since we want to return max CHUNKS not max SPLITS!!!
        res = 1
        cur_max = float("-inf")
        for i in range(len(arr) - 1):
            cur_max = max(cur_max, arr[i])
            if cur_max <= suffix_min[i + 1]:
                res += 1
                cur_max = float("-inf")
        return res
