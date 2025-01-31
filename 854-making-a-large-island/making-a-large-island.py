class Solution:
    def generateUniqueIslandId(self):
        self.island_id += 1
        return self.island_id - 1

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.pos_to_island = defaultdict(lambda: None)
        self.island_to_area = {None: 0}
        self.island_id = 0
        N = len(grid)
        WATER, LAND = 0, 1
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]

        res = self.maxAreaOfIsland(grid)
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
                    bordering_islands.add(self.pos_to_island[(x, y)])

                area = 1
                for island in bordering_islands:
                    area += self.island_to_area[island]
                
                # Update max area!
                if res < area:
                    res = area

        return res
    
    def maxAreaOfIsland(self, grid):
        N = len(grid)
        max_area = 0
        global_visited = set()
        WATER, LAND = 0, 1
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        inBounds = lambda x, y: 0 <= x < N and 0 <= y < N
        for i in range(N):
            for j in range(N):
                if grid[i][j] == WATER or (i, j) in global_visited:
                    continue

                island_id = self.generateUniqueIslandId()                
                area = 0
                visited = set()
                visited.add((i, j))
                stack = [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()
                    self.pos_to_island[(x, y)] = island_id
                    area += 1

                    for dx, dy in DIRECTIONS:
                        neigh_x, neigh_y = x + dx, y + dy
                        if not inBounds(neigh_x, neigh_y):
                            continue
                        if (neigh_x, neigh_y) in visited:
                            continue
                        if grid[neigh_x][neigh_y] == WATER:
                            continue
                        visited.add((neigh_x, neigh_y))
                        stack.append((neigh_x, neigh_y))
                

                # if modify_perimiter:
                #     for i, j in visited:
                #         for di, dj in DIRECTIONS:
                #             x, y = i + di, j + dj
                #             if inBounds(x, y) and (x, y) not in visited and grid[x][y] == WATER:
                #                 self.perimiter.add((x, y))
                
                assert len(visited) == area
                self.island_to_area[island_id] = area
                max_area = max(max_area, area)
                global_visited.update(visited)

                # For every visited position in the island, let's see how large of a BFS
                # we can extend outwards from it!
                # for i, j in visited:
                #     for di, dj in DIRECTIONS:
                #         x, y = i + di, j + dj
                #         if inBounds(x, y) and (x, y) not in visited and grid[x][y] == WATER:
                #             # Run a BFS from this x,y to catch as MANY visited land cells as possible!
                #             stack = [(i, j)]
                #             extra_visited = set([(i, j)])
                #             isVisited = lambda pos: pos in global_visited or pos in extra_visited

                #             while len(stack) > 0:
                #                 x, y = stack.pop()

        
        return max_area
