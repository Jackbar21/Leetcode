class Solution:
    # Step 2: Simple UCS to find optimal cost from 'source' to GOAL_NODE
    def ucs(self, source):
        GOAL_NODE = self.n - 1
        fringe = [(0, source)] # (cost, node) | min-heap/priority-queue (i.e. UCS)
        visited = set()
        optimal_cost = float("inf")
        while len(fringe) > 0:
            cost, node = heapq.heappop(fringe)
            if node in visited:
                # Already found shortest path to it!
                continue
            visited.add(node)
            if node == GOAL_NODE:
                # Optimal cost!
                return cost
            
            for neigh, time in self.adj_list[node]:
                if neigh not in visited:
                    heapq.heappush(fringe, (cost + time, neigh))
        
        raise Exception("No path found!")

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        self.n = n
        MOD = pow(10, 9) + 7

        # Step 1: Build adjacency list!
        adj_list = {node: [] for node in range(n)}
        for u, v, time in roads:
            adj_list[u].append((v, time))
            adj_list[v].append((u, time))
        self.adj_list = adj_list

        # Step 2: Simple UCS to find optimal cost
        shortest_paths = {node: self.ucs(node) for node in range(n)}
        self.shortest_paths = shortest_paths
        # print(f"{self.shortest_paths=}")
        # return self.ucs(3 if n >= 3 else 0)
        # return -1

        # We know have shortest path of
        # print(f"{shortest_paths=}")
        self.shortest_paths = shortest_paths
        return self.dp(0, shortest_paths[0]) % MOD
        return -1
    
    @cache
    def dp(self, node, cost):
        GOAL_NODE = self.n - 1
        if cost <= 0:
            return cost == 0 and node == GOAL_NODE
        
        if self.shortest_paths[node] > cost:
            # print(f"{node, cost, self.shortest_paths=}")
            return 0

        res = 0
        for neigh, time in self.adj_list[node]:
            # if cost - time - self.shortest_paths[neigh] >= 0:
            if cost - time >= 0:
                res += self.dp(neigh, cost - time)
        
        return res
