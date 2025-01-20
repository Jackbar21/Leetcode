class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        # Idea: Loop through all elements in mat, and use a hash-map to store the value and have
        # them map to their position in mat. Then we can loop over arr, and paint things on the go
        # using O(1) look-up times with the hash-map. Then, everytime we paint something, we add that
        # element to it's corresponding row & column "painted positions", and at any point if a row
        # contains N painted positions or a column contains M painted positions, we know we are done
        # with the problem! And at that point, return the current index we just used to paint with
        # last in arr :)

        # Step 1: Loop through mat, mapping val-to-position values in d
        # d = {}
        d = [None] * (M * N + 1)
        for i in range(M):
            for j in range(N):
                # Since values in mat are strictly [1, m * n], there are no duplicate values!
                # TODO: IN FACT: This means we don't even need a dictionary/hash-map, can just use an array!
                val = mat[i][j]
                d[val] = (i, j)
        
        # Step 2: We have M rows, and N columns. We need to create a unique dictionary for each row,
        # and each column, each mapping to # of painted positions in that row / column!
        rows = defaultdict(int)
        columns = defaultdict(int)
        for index, val in enumerate(arr):
            i, j = d[val]
            rows[i] += 1
            columns[j] += 1
            if rows[i] == N or columns[j] == M:
                return index
        
        raise Exception("Unreachable Code!")


