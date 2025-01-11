class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Idea: I recognize this to be an extremely convenient use case
        # of the MST (Minimum-Spanning-Tree) construction algorithms, e.g.
        # Prim's or Kruskal's. For Kruskal's I've now realized I probably
        # end up needing to use something like Disjoint Sets in order to
        # verify whether greedily adding an edge introduces a cycle in the
        # graph (by calling FIND on two nodes of interest), which I'm too
        # lazy to implement... hence I went down the Prim's algorith path haha xD
        # return self.prim(points)
        return self.kruskal(points)
    
    def manhattenDistance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x2 - x1) + abs(y2 - y1)

    def prim(self, points: List[List[int]]) -> int:
        N = len(points)
        points = list(map(tuple, points))

        # Step 1: Build an adjacency list for all the points
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pos1, pos2 = points[i], points[j]
                cost = self.manhattenDistance(pos1, pos2)
                edges.append((cost, pos1, pos2))

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
        mst_edges_count = 0
        mst_cost = 0
        while mst_edges_count < N - 1:
            cost, node, neigh = heapq.heappop(edges_available)
            # assert node in visited
            if neigh in visited:
                continue
            
            # Confirm edge as part of solution
            visited.add(neigh)
            mst_cost += cost
            mst_edges_count += 1

            # Now, introduce all available edges from neigh!
            for edge_cost, new_neigh in adj_list[neigh]:
                if new_neigh not in visited:
                    heapq.heappush(edges_available, (edge_cost, neigh, new_neigh))
        
        return mst_cost

        """
        EXAMPLE WALKTHROUGH (from video!):
        N = 5
        visited = {(3,10), (2,2), (0,0), (5,2), (7,0)}

        edges = [
            (3,10) --> (0,0), cost=13
            (3,10) --> (5,2), cost=10
            (3,10) --> (7,0), cost=14,
            (2,2)  --> (7,0), cost=7,
            (0,0)  --> (5,2), cost=7,
            (0,0)  --> (7,0), cost=7,
        ]

        MST_EDGES = [
            (3,10) --> (2,2), cost=9
            (2,2)  --> (0,0), cost=4
            (2,2)  --> (5,2), cost=3,
            (5,2)  --> (7,0), cost=4
        ]

        """
    
    def kruskal(self, points: List[List[int]]) -> int:
        N = len(points)
        points = list(map(tuple, points))

        disjoint_set = {point: point for point in points}
        def find(point):
            while point != disjoint_set[point]:
                point = disjoint_set[point]
            return point
        # def union(point1, point2):
        #     parent1, parent2 = find(point1), find(point2)
        #     disjoint_set[parent2] = parent1

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pos1, pos2 = points[i], points[j]
                cost = self.manhattenDistance(pos1, pos2)
                edges.append((cost, pos1, pos2))
        heapq.heapify(edges)

        mst_cost = 0
        mst_edges_count = 0
        while mst_edges_count < N - 1:
            cost, pos1, pos2 = heapq.heappop(edges)
            parent1, parent2 = find(pos1), find(pos2)
            if parent1 == parent2:
                continue
            
            mst_cost += cost
            mst_edges_count += 1
            disjoint_set[parent2] = parent1 # Union sets!
        
        return mst_cost


