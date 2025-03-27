class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        START, GOAL = (0, 0), (N - 1, N - 1)
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inBounds = lambda x, y: 0 <= x < N and 0 <= y < N

        fringe = [(grid[0][0], 0, 0)] # min-heap | (cost, i, j)
        visited = set()
        while len(fringe) > 0:
            #print(f"{fringe=}")
            cost, i, j = heapq.heappop(fringe)
            #print(f"{cost, i, j=}")
            
            if (i, j) in visited:
                continue
            visited.add((i, j))

            # Check if found goal state!
            if (i, j) == GOAL:
                return cost

            for di, dj in DIRECTIONS:
                neigh_i, neigh_j = i + di, j + dj
                if not inBounds(neigh_i, neigh_j):
                    continue
                #print(f"{cost, grid[neigh_i][neigh_j], neigh_i, neigh_j=}, {(neigh_i, neigh_j) in visited=}")
                if (neigh_i, neigh_j) in visited:
                    continue
                # if cost < (neigh_cost := grid[neigh_i][neigh_j]):
                #     cost = neigh_cost
                heapq.heappush(fringe, (max(cost, grid[neigh_i][neigh_j]), neigh_i, neigh_j))

