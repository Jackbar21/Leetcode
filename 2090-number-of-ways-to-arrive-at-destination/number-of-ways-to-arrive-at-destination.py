class Solution:
    # Step 2: Simple UCS to find optimal cost from 'source' to GOAL_NODE
    @cache
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
        # self.shortest_paths = {node: self.ucs(node) for node in range(n)}
        self.dp_memo = {}
        return self.dp(0, self.ucs(0)) % MOD
    
    # @cache
    def dp(self, node, cost):
        if (node, cost) in self.dp_memo:
            return self.dp_memo[(node, cost)]

        if cost <= 0:
            # assert cost == 0
            GOAL_NODE = self.n - 1
            return node == GOAL_NODE
        
        shortest_path = self.ucs(node)
        if shortest_path > cost:
            return 0

        res = 0
        for neigh, time in self.adj_list[node]:
            if cost - time >= 0:
                res += self.dp(neigh, cost - time)
        
        self.dp_memo[(node, cost)] = res
        return res
