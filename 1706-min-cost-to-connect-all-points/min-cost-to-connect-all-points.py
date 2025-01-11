class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Idea: I recognize this to be an extremely convenient use case
        # of the MST (Minimum-Spanning-Tree) construction algorithms, e.g.
        # Prim's or Kruskal's.
        # return self.kruskal(points)
        return self.prim(points)
    
    def manhattenDistance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x2 - x1) + abs(y2 - y1)


    def kruskal(self, points: List[List[int]]) -> int:
        N = len(points)

        # Step 1: Add all edges to a priority queue.
        # To do this, we need to loop over all O(N^2) possible
        # edges, and include their cost every time!
        min_heap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pos1, pos2 = tuple(points[i]), tuple(points[j])
                cost = self.manhattenDistance(pos1, pos2)
                min_heap.append((cost, pos1, pos2))
        heapq.heapify(min_heap) # O(E) [where E = O(N^2)]

        mst_cost = 0
        res_edges = []
        connected_nodes = set()
        while len(min_heap) > 0 and len(connected_nodes) < N:
            cost, pos1, pos2 = heapq.heappop(min_heap)

            # Edge must connect at least ONE new node! Otherwise, it is irrelevant!
            if pos1 in connected_nodes and pos2 in connected_nodes:
                continue
            
            connected_nodes.add(pos1)
            connected_nodes.add(pos2)
            mst_cost += cost
            res_edges.append(f"{pos1} --> {pos2}")
            
        # print(f"{len(connected_nodes)=}, {N=}")
        # print(f"{res_edges=}")
        return mst_cost


    def prim(self, points: List[List[int]]) -> int:
        N = len(points)
        # points = list(map(tuple, points))
        points = [tuple(point) for point in points]

        # Step 1: Build an adjacency list for all the points
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pos1, pos2 = points[i], points[j]
                cost = self.manhattenDistance(pos1, pos2)
                edges.append((cost, pos1, pos2))
        
        if len(edges) == 0:
            return 0

        min_edge = min(edges)
        # # print(f"{min_edge=}")

        adj_list = defaultdict(list)
        for cost, pos1, pos2 in edges:
            adj_list[pos1].append((cost, pos2))
            adj_list[pos2].append((cost, pos1))

        # Step 2: Pick any node to start from, as it must be included in the final
        # MST anywy lol :P
        random_index = random.randint(0, N - 1)
        node = points[random_index]
        


        # We need to keep going until we have N - 1 total edges!
        visited = set([node])
        edges_available = [(cost, node, neigh) for cost, neigh in adj_list[node]]
        heapq.heapify(edges_available)
        mst_edges = set()
        mst_cost = 0
        while len(mst_edges) < N - 1:
            cost, node, neigh = heapq.heappop(edges_available)
            if (cost, node, neigh) in mst_edges:
                continue
            assert node in visited
            if neigh in visited:
                continue
            
            # print(f"{cost, node, neigh=}")
            
            # Confirm edge as part of solution
            visited.add(neigh)
            mst_cost += cost
            mst_edges.add((cost, node, neigh))

            # Now, introduce all available edges from neigh!
            for edge_cost, new_neigh in adj_list[neigh]:
                if new_neigh in visited:
                    continue
                
                heapq.heappush(edges_available, (edge_cost, neigh, new_neigh))
        
        # # print(f"{mst_edges=}")
        return mst_cost

