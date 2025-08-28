class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        N = len(grid)
        for i in range(N):
            for j in range(N):
                id = j - i
                d[id].append((grid[i][j], i, j))

        #print(d)
        for key in d:
            d[key].sort(reverse = key <= 0)
        
        pointers = defaultdict(int)
        for i in range(N):
            for j in range(N):
                id = j - i
                pointer = pointers[id]
                pointers[id] += 1
                val = d[id][pointer][0]
                grid[i][j] = val

        return grid