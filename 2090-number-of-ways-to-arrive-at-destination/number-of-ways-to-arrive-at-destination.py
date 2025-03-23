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
            if cost - time - self.shortest_paths[neigh] >= 0:
            # if cost - time >= 0:
                res += self.dp(neigh, cost - time)
        
        return res

        
    #     visited = set()
    #     res = 0
    #     # Step 3 ZONE
    #     solutions = defaultdict(int)
    #     fringe = collections.deque([(0, 0)])
    #     solutions[(0, 0)] += 1
    #     visited_edges = set()
    #     while len(fringe) > 0:
    #         cost, node = fringe.popleft()
    #         # solutions[(node, cost)] += 1
    #         assert not ((node == GOAL_NODE) and (cost < optimal_cost))
    #         # res += (node == GOAL_NODE) and (cost <= optimal_cost)

    #         for neigh, time in adj_list[node]:
    #             solutions[(neigh, cost + time)] += 1
    #             edge = (node, neigh, time)
    #             # if neigh in visited or cost + time > optimal_cost:
    #             #     continue
    #             if edge in visited_edges:
    #                 continue
    #             visited_edges.add(edge)
    #             fringe.append((cost + time, neigh))
    #         # visited.add(node)

    #     print(f"{solutions=}")
    #     res = solutions[(GOAL_NODE, optimal_cost)] % MOD
    #     return res

    #     self.adj_list = adj_list
    #     self.GOAL_NODE = GOAL_NODE
    #     self.memo = {}
    #     return self.dp(0, optimal_cost)
    #     # return -1
    
    # @cache
    # def dp(self, node, cost):
    #     # if (node, cost) in self.memo:
    #     #     return self.memo[(node, cost)]

    #     if cost <= 0:
    #         return node == self.GOAL_NODE
        
    #     res = 0
    #     for neigh, time in self.adj_list[node]:
    #         if cost - time >= 0:
    #             res += self.dp(neigh, cost - time)
        
    #     # self.memo[(node, cost)] = res
    #     return res

    # # @cache
    # # def dp(self, node, visited):
    # #     tuple_visited = tuple(visited)
    # #     if (node, tuple_visited) in self.memo:
    # #         return self.memo[(node, tuple_visited)]

    # #     if node == self.GOAL_NODE:
    # #         return 1
        
    # #     res = 0
    # #     for neigh, time in self.adj_list[node]:
    # #         if neigh in visited:
    # #             continue
    # #         visited.add(neigh)
    # #         res += self.dp(neigh, visited)
    # #         visited.remove(neigh)
        
    # #     return res

    #     """

    #     # Idea: BFS and exhaust all edges from every node
    #     res = 0
    #     queue = collections.deque([(0, 0)])
    #     # print(f"{optimal_cost=}, {GOAL_NODE=}")
    #     visited = set()
    #     while queue:
    #         cost, node = queue.popleft()
    #         # print(f"{cost, node=}")
    #         if cost > optimal_cost:
    #             continue
    #         if node == GOAL_NODE:
    #             res += 1
    #             continue

    #         # Populate every unvisited neighbor into queue
    #         for neigh, time in adj_list[node]:
    #             if cost + time <= optimal_cost:
    #                 queue.append((cost + time, neigh))
    #                 # DO NOT MARK NEIGH VISITED
    #         visited.add(node)
        
    #     return res

    #     # Traverse the graph continuously until you've used up ALL edges. Count
    #     # the number of times you hit the goal node with 'optimal_cost' time!
    #     res = 0
    #     fringe = collections.deque([(0, 0)])
    #     visited = set()
    #     visited_edges = set()
    #     while fringe:
    #         cost, node = fringe.popleft()
    #         # if cost > optimal_cost:
    #         #     continue
    #         # if node == GOAL_NODE:
    #         res += (node == GOAL_NODE) and (cost <= optimal_cost)

    #         for neigh, time in adj_list[node]:
    #             edge = (node, neigh, time)
    #             if edge in visited_edges:
    #                 continue
    #             visited_edges.add((node, neigh, time))
    #             visited_edges.add((neigh, node, time))
    #             fringe.append((cost + time, neigh))
        
    #     return res


        
    #     # Step 3: Count all the paths to GOAL_NODE whose cost is equal to optimal cost
    #     res = 0
    #     visited = set([0])
    #     fringe = collections.deque([(0, 0)]) # (cost, node)
    #     while fringe:
    #         cost, node = fringe.popleft()
    #         if cost > optimal_cost:
    #             continue

    #         if node == GOAL_NODE:
    #             assert cost == optimal_cost
    #             res += 1
    #             continue
            
    #         for neigh, time in adj_list[node]:
    #             if neigh in visited:
    #                 continue
    #             fringe.append((cost + time, neigh))
        
    #     return res
            

    #     # fringe = collections.deque([(0, 0, set([0]))]) # (cost, node) | queue (i.e. BFS)
    #     # while len(fringe) > 0:
    #     #     cost, node, visited = fringe.popleft()
    #     #     if node == GOAL_NODE:
    #     #         res += 1
    #     #         continue
            
    #     #     for neigh, time in adj_list[node]:
    #     #         if neigh in visited:
    #     #             continue

    #     #         new_cost = cost + time
    #     #         if new_cost > optimal_cost:
    #     #             continue

    #     #         visited.add(neigh)
    #     #         fringe.append((new_cost, neigh, visited))
        
    #     return res % MOD
    #     """