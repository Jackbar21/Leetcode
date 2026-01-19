class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        M, N = len(mat), len(mat[0])
        res = 0
        for i in range(M):
            for j in range(N):
                cur_sum = mat[i][j]
                length = 1
                while cur_sum <= threshold:
                    res = max(res, length)
                    if i + length >= M or j + length >= N:
                        break
                    
                    for idx in range(i, i + length + 1):
                        cur_sum += mat[idx][j + length]
                    for idx in range(j, j + length + 1):
                        cur_sum += mat[i + length][idx]
                    cur_sum -= mat[i + length][j + length] # double counted
                    length += 1
        
        return res