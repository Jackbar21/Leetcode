class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            val = matrix[i][j]
            
            res = 1
            for di, dj in DIRECTIONS:
                neigh_i, neigh_j = i + di, j + dj
                if not inBounds(neigh_i, neigh_j):
                    continue
                
                # Don't have to worry about infinite cycles (i.e. re-visiting nodes)
                # since path must be STRICTLY increasing. So if we can go from u->v,
                # because v is LARGER than u, then we cannot go back via v->u. Therefore
                # this forms a DAG, and we can apply DP safely :)
                neigh_val = matrix[neigh_i][neigh_j]
                if neigh_val > val:
                    res = max(res, 1 + dp(neigh_i, neigh_j))
            
            memo[(i, j)] = res
            return res

        return max(dp(i, j) for i in range(M) for j in range(N))
