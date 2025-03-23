class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        self.n = n
        self.roads = roads
        MOD = pow(10, 9) + 7
        # dp = self.floydWarshall()
        # self.getShortestPath = lambda source, dest: dp[source][dest]

        # Step 1: Build adjacency list!
        adj_list = {node: [] for node in range(n)}
        for u, v, time in roads:
            adj_list[u].append((v, time))
            adj_list[v].append((u, time))
        self.adj_list = adj_list

        # Step 2: Compute number of ways to get from 0 to goal node in 'optimal_cost' time!
        optimal_cost = self.ucs(0)
        return self.dp(0, optimal_cost) % MOD
    
    @cache
    def dp(self, node, budget):
        if budget <= 0:
            GOAL_NODE = self.n - 1
            return (budget == 0) and (node == GOAL_NODE)
        
        shortest_path_cost = self.ucs(node)
        if budget < shortest_path_cost:
            return 0

        res = 0
        for neigh, time in self.adj_list[node]:
            res += self.dp(neigh, budget - time)
        return res

    # Simple UCS to find optimal cost from 'source' to GOAL_NODE
    @cache
    def ucs(self, source):
        GOAL_NODE = self.n - 1
        fringe = [(0, source)] # (cost, node) | min-heap/priority-queue (i.e. UCS)
        visited = set()
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
    
    # I figured Floyd-Warshall algo might be faster since edges can be at most O(N^2),
    # and similar to Johnson's algorithm, we pretty much 'run Dijkstra's N times' in this
    # problem (via ucs function) which is worse in dense graphs (i.e. |E| == O(|V|^2)) than
    # Floyd-Warshall. But, to my surprise, Floyd-Warshall performed worse, so I'm not using it
    # but wanted to keep the code here just for fun :)
    def floydWarshall(self):
        n = self.n
        dp = [[float("inf")] * n for _ in range(n)]
        
        for u, v, time in self.roads:
            dp[u][v] = time
            dp[v][u] = time
        
        for i in range(n):
            dp[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cost = dp[i][k] + dp[k][j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        return dp
