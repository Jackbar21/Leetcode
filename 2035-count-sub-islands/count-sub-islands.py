class Solution:
    def __init__(self):
        self.grid1, self.grid2 = None, None
        self.m, self.n = None, None
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.grid1, self.grid2 = grid1, grid2
        self.m, self.n = len(self.grid2), len(self.grid2[0])
        WATER, LAND = 0, 1
        num_sub_islands = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid2[i][j] == LAND:
                    # is_sub_island defaulted to True, and value set to
                    # False if any corresponding cell inside grid2 island
                    # happens to be a WATER (i.e. non-LAND) cell.
                    num_sub_islands += self.populateIsland(i, j, True)
                    
        return num_sub_islands

    def populateIsland(self, i, j, is_sub_island):
        WATER, LAND = 0, 1
        assert self.grid2[i][j] == LAND
        
        # Instead of using visited set, update found LAND into WATER cells directly.
        self.grid2[i][j] = WATER
        if self.grid1[i][j] == WATER:
            is_sub_island = False
        
        # Recursively update neighbors that are also LAND cells.
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for (di, dj) in directions:
            new_i, new_j = (i + di, j + dj)
            if (0 <= new_i < self.m 
                and 0 <= new_j < self.n
                and self.grid2[new_i][new_j] == LAND
            ):
                is_sub_island = self.populateIsland(new_i, new_j, is_sub_island)
        
        return is_sub_island