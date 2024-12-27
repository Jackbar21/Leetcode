class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # max_val = float("-inf")
        # for i in range(len(values)):
        #     for j in range(i + 1, len(values)):
        #         max_val = max(max_val , values[i] + values[j] + i - j)
        # return max_val
        # self.memo = {}
        # return self.dp(0, len(values) - 1)

        cur_max = float("-inf")
        cur_dist = 0
        suffix_max = collections.deque([cur_max])
        for r in range(len(values) - 1, -1, -1):
            cur_max = max(cur_max, values[r] - r)
            suffix_max.appendleft(cur_max)

        suffix_max.popleft()
        # print(f"{suffix_max=}")
        # return 0

        res = float("-inf")
        for i in range(len(values)):
            res = max(res, values[i] + i + suffix_max[i])
            # print(f"{res=}")
        return res
