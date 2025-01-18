class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4
        DIRECTIONS = [RIGHT, LEFT, DOWN, UP]
        direction_to_delta = {
            RIGHT: (0, 1),
            LEFT: (0, -1),
            DOWN: (1, 0),
            UP: (-1, 0)
        }
        M, N = len(grid), len(grid[0])
        inBounds = lambda x, y: 0 <= x < M and 0 <= y < N

        fringe = [(0, 0, 0)] # (cost, x, y) -- min heap for UCS! Might be able to 0-1 BFS instead
        visited = set()

        while len(fringe) > 0:
            cost, x, y = heapq.heappop(fringe)
            sign = grid[x][y]

            if x == M - 1 and y == N - 1:
                # Found goal, return minimum cost!
                return cost

            if (x, y) in visited:
                continue
            visited.add((x, y))

            for direction in DIRECTIONS:
                dx, dy = direction_to_delta[direction]
                neigh_x, neigh_y = x + dx, y + dy
                if not inBounds(neigh_x, neigh_y):
                    continue
                
                if (neigh_x, neigh_y) in visited:
                    continue

                # if direction == sign:
                #     # This is node's actual neighbor!
                #     adj_list[node].add((neigh_i, neigh_j))
                #     adj_list[clone_node].add((neigh_i + M, neigh_j + N))
                # else:
                #     adj_list[node].add((neigh_i + M, neigh_j + N))
                added_cost = 0 if direction == sign else 1
                heapq.heappush(fringe, (cost + added_cost, neigh_x, neigh_y))
            


    
    def minCostVassos(self, grid):
        RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4
        DIRECTIONS = [RIGHT, LEFT, DOWN, UP]
        direction_to_delta = {
            RIGHT: (0, 1),
            LEFT: (0, -1),
            DOWN: (1, 0),
            UP: (-1, 0)
        }
        M, N = len(grid), len(grid[0])

        def getDirectionDeltas(direction):
            return DIRECTIONS[direction - 1]

        # This is ALMOST a near-exact-replica of my FAVOURITE computer science problem of ALL TIME!!!
        # The idea is to essentially construct this as a graph G , then construct a new graph G' as follows:
        #   (1) Keep each node u in G, alongside every edge (u,v) in G
        #   (2) For each node u in G, create a clone-node u'
        #   (3) For each edge from u to v of G, create an edge from u' to v'
        #   (4) For each edge from u to v in G with sign c, create edge from u to v' for each sign != c

        # Since grid is m x n, we can denote that a node u in G will be a pair (i, j) in 'grid'. We can
        # use the pair (i + m, j + n) to denote the copy node u'.
        adj_list = defaultdict(set) # node to neighbors-set
        for i in range(M):
            for j in range(N):
                node = (i, j)
                clone_node = (i + M, j + N)
                sign = grid[i][j]

                for direction in DIRECTIONS:
                    di, dj = direction_to_delta[direction]
                    neigh_i, neigh_j = i + di, j + dj
                    if direction == sign:
                        # This is node's actual neighbor!
                        adj_list[node].add((neigh_i, neigh_j))
                        adj_list[clone_node].add((neigh_i + M, neigh_j + N))
                    else:
                        adj_list[node].add((neigh_i + M, neigh_j + N))

        # Now, want to UCS from position (0, 0), but now there are TWO possible goal states:
        #   (1) (m - 1, n - 1), Original Goal State!
        #   (2) (m - 1 + m, n - 1 + n), Clone of Original Goal State!
        ORIGINAL_GOAL_STATE = (M - 1, N - 1)
        CLONE_GOAL_STATE = (M - 1 + M, N - 1 + N)
        GOAL_STATES = set([ORIGINAL_GOAL_STATE, CLONE_GOAL_STATE])

        fringe = [(0, 0, 0)] # min-heap for UCS! (cost, x, y)
        # while len(fringe) > 0:



