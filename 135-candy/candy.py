class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        adj_list = [[] for i in range(N)]
        for i in range(len(ratings)):
            prev = ratings[i - 1] if i > 0 else float("inf")
            cur = ratings[i]
            nxt = ratings[i + 1] if i + 1 < N else float("inf")

            if cur > prev:
                # cur (index i) needs MORE candy than prev (index i - 1)
                adj_list[i].append(i - 1)
            
            if cur > nxt:
                # cur (index i) needs MORE candy than prev (index i - 1)
                adj_list[i].append(i + 1)

        memo = {}
        def dp(node):
            if node in memo:
                return memo[node]

            if len(adj_list[node]) == 0:
                return 1 # Doesn't need more candy than anybody else, so just 1 candy!
            
            res = 1 + max(dp(neigh) for neigh in adj_list[node])
            memo[node] = res
            return res
        
        return sum(dp(i) for i in range(N))