class Solution:

    @cache
    def dp(self, node, edges_left):
        if node == self.dst:
            return 0

        if edges_left == 0:
            return float("inf")
        
        res = float("inf")
        for neigh, price in self.adj_list[node]:
            path_cost = price + self.dp(neigh, edges_left - 1)
            if path_cost < res:
                res = path_cost
        return res


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k stops <==> k + 1 edges!
        MAX_EDGE_COUNT = k + 1

        # Step 1: Build adjacency list (with edge weights!)
        adj_list = defaultdict(list)
        for source, dest, price in flights:
            adj_list[source].append((dest, price)) # (neigh, price)
        self.adj_list = adj_list
        self.n = n
        self.src = src
        self.dst = dst
        self.k = k
        res = self.dp(src, k + 1)
        return res if res != float("inf") else -1

        fringe = [(0, 0, src)] # (cost, edge_count, node)
        # visited = set([src])
        # visited_edges = set()
        while len(fringe) > 0:
            #print(f"{fringe=}")
            cost, edge_count, node = heapq.heappop(fringe)
            if edge_count > MAX_EDGE_COUNT: 
                continue
            # if node in visited:
            #     continue
            # visited.add(node)

            # assert edge_count <= k
            if node == dst:
                return cost
            
            # if edge_count == k:
            #     # Visiting any neighbors would surpass the edge limit of k,
            #     # so continue with loop instead!
            #     continue
        
            # Otherwise, go through neighbors!
            for neigh, price in adj_list[node]:
                # if (node, neigh) in visited_edges:
                #     continue
                # visited_edges.add((node, neigh))
                # if not (edge_count + 1 <= k):
                #     break
                # if neigh not in visited:
                heapq.heappush(fringe, (cost + price, edge_count + 1, neigh))
                # visited.add(neigh)

        #print(f"{visited_edges=}")
        return -1

#  0 --(1)--> 1
#  |        /
# (5)    /(1)  
#  |  /
#  v V
#  2 --(1)--> 3