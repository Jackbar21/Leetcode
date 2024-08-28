class Solution:
    def __init__(self):
        # self.visited = set() # Visited land slots in grid2
        self.grid1 = None
        self.grid2 = None
        self.m = None
        self.n = None
        self.sub_islands = 0
        self.num_islands = 0
        self.is_sub_island = True
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        WATER, LAND = 0, 1
        self.grid1, self.grid2 = grid1, grid2
        self.m, self.n = len(self.grid2), len(self.grid2[0])
        num_sub_islands = 0
        num_islands = 0     # For debugging purposes, remove later
        for i in range(self.m):
            for j in range(self.n):
                if self.grid2[i][j] == WATER:
                    continue
                else:
                    num_sub_islands += self.populateIsland(i, j)
                    num_islands += 1
                    continue
        
        # print(f"{num_islands=}, {num_sub_islands=}")
        return num_sub_islands
                
                # We just hit on a land.
                # assert self.grid2[i][j] == LAND
                
                # is_sub_island = True # Default value, can change!
                # self.grid2[i][j] = WATER
                # if self.grid1[i][j] == WATER:
                #     is_sub_island = False
                # We want to "populate" the island, by adding
                # converting all land-cells we see connected to this
                # LAND slot into WATER slots. Note that we could also
                # achieve this by populating a visited set, but doing
                # so this way allows us to reutilize memory in-place.
                # directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                # for (di, dj) in directions:
                #     new_i, new_j = (i + di, j + dj)
                #     if (0 <= new_i < self.m 
                #         and 0 <= new_j < self.n
                #         and self.grid2[new_i][new_j] == LAND
                #         # and (new_i, new_j) not in self.visited
                #     ):
                #         self.grid2[new_i][new_j] = WATER
                #         if self.grid1[new_i][new_j] == WATER:
                #             is_sub_island = False


    # "Populates" an island starting from position (i, j) in grid2
    # (which must be a LAND cell) by replacing 
    def populateIsland(self, i, j, is_sub_island = True):
        WATER, LAND = 0, 1
        assert self.grid2[i][j] == LAND
        
        # Instead of visited set, change LAND cells to WATER directly.
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
                # and (new_i, new_j) not in self.visited
            ):
                # self.grid2[new_i][new_j] = WATER
                # if self.grid1[new_i][new_j] == WATER:
                #     is_sub_island = False
                is_sub_island = self.populateIsland(new_i, new_j, is_sub_island)
        
        return is_sub_island

