class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.island_id = 0
        def generateUniqueIslandId():
            self.island_id += 1
            return self.island_id
        
        N = len(grid)
        WATER, LAND = 0, 1
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        pos_to_island = {} # map (x, y) positions in grid to island id
        island_to_area = {None: 0} # map island id to area / size of that island
        
        # Step 1: Get initial max island in grid, and populate 'pos_to_island'
        # and 'island_to_area' dicitonaries in doing so!
        res = 0
        visited = set()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == WATER or (i, j) in visited:
                    continue

                island_id = generateUniqueIslandId()
                area = 0
                visited.add((i, j))
                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()
                    pos_to_island[(x, y)] = island_id
                    area += 1

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy
                        if (0 <= neigh_x < N and 0 <= neigh_y < N
                            and (neigh_x, neigh_y) not in visited 
                            and grid[neigh_x][neigh_y] == LAND
                        ):
                            visited.add((neigh_x, neigh_y))
                            stack.append((neigh_x, neigh_y))

                island_to_area[island_id] = area
                if res < area:
                    res = area

        # Step 2: Loop through all the water cells, and compute the new maximum island size
        # if that water cell is turned into an island! This is done by looking at the water
        # cells directly-adjacent neighbors, and getting those neighbor's corresponding island id
        # (if they are in an island). Then, each found island id from these 4 neighbors can be joined
        # together, so the new area will simply be 1 + sum of each directly reachable island size for
        # every WATER cell in grid!
        for i in range(N):
            for j in range(N):
                if grid[i][j] == LAND:
                    continue
                
                # Since we are a WATER cell, we have the potential of CONNECTING it
                # to other islands! Hence, we will look at this positions neighbors,
                # to consider all the islands it connects! Then the max size will be
                # 1 for this node (as it was turned into LAND from WATER), plus the
                # size of EACH UNIQUE ISLAND it borders!!
                bordering_islands = set()
                for di, dj in DIRECTIONS:
                    x, y = i + di, j + dj
                    bordering_islands.add(pos_to_island.get((x, y), None))

                area = 1
                for island in bordering_islands:
                    area += island_to_area[island]
                
                # Update max area!
                if res < area:
                    res = area

        return res
