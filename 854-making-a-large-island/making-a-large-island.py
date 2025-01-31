class Solution:
    def generateUniqueIslandId(self):
        self.island_id += 1
        return self.island_id - 1

    def largestIsland(self, grid: List[List[int]]) -> int:
        # Idea: For each position in grid, we will denote the unique island it maps to,
        # as well as its size! We can use something like disjoint sets for it, or since
        # I'm lazy a unique ID for each!
        self.pos_to_island = defaultdict(lambda: None)
        self.island_to_pos = {None: set()}
        self.island_id = 0
        N = len(grid)
        WATER, LAND = 0, 1
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        self.perimiter = set()
        res = self.maxAreaOfIsland(grid)
        print(f"{self.pos_to_island=}")
        print(f"{self.island_to_pos=}")
        inBounds = lambda x, y: 0 <= x < N and 0 <= y < N

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
                # area = 1 + functools.reduce(lambda island: len(self.island_to_pos[island]), bordering_islands)
                area = 1
                for island in bordering_islands:
                    area += len(self.island_to_pos[island])
                res = max(res, area)
        return res

        # for i in range(N):
        #     for j in range(N):
        #         if grid[i][j] == WATER:
        #         # if (i, j) in self.perimiter:
        #             grid[i][j] = LAND
        #             res = max(res, self.maxAreaOfIsland(grid))
        #             grid[i][j] = WATER
        
        # Now that we have visited the full island, we want to consider every water cell that
        # touches the island (but not in the island itself), and see if turning that water cell
        # into an island touches an island with a DIFFERENT id! For each case, we will consider
        # what happens, since we either only increment the island size by 1, OR we end up
        # incrementing the island size by not only 1, but the other touching island!
        for island_id, visited in self.island_to_pos.items():
            area = len(visited)

            perimiter = set()
            for i, j in visited:
                for di, dj in DIRECTIONS:
                    x, y = i + di, j + dj
                    if inBounds(x, y) and (x, y) not in visited and grid[x][y] == WATER:
                        perimiter.add((x, y))
            
            # Now for each perimiter node, we could effectively set it to 1 to increase the
            # size of the area by one!
            # if len(perimiter) > 0:
            #     area += 1
            # # But, if ANY of them are capable of touching an island (or even multiple islands)
            # # that are NOT the original island
            # for x, y in perimiter:

            
            # while len(perimiter) > 0:
            #     i, j = perimiter.pop()
            #     extra_area = 0
            #     stack = [(i, j)]
            #     extra_visited = set()
            #     isVisited = lambda x, y: (x, y) in visited or (x, y) in extra_visited

            #     while len(stack) > 0:
            #         x, y = stack.pop()
            #         extra_area += 1

            #         for dx, dy in DIRECTIONS:
            #             neigh_x, neigh_y = x + dx, y + dy
            #             if not inBounds(neigh_x, neigh_y):
            #                 continue
            #             if isVisited(neigh_x, neigh_y):
            #                 continue
            #             if grid[neigh_x][neigh_y] == WATER:
            #                 continue
                        
            #             extra_visited.add((neigh_x, neigh_y))
            #             stack.append((neigh_x, neigh_y))
        
        if res < 1:
            return 1
        if res > N * N:
            return N * N
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
                self.island_to_pos[island_id] = visited
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
