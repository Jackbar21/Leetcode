class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        # adj_list = [[] for _ in range(N)]
        # for i, neigh in enumerate(edges):
        #     if neigh != -1:
        #         adj_list[i].append(neigh)
        # self.N, self.adj_list = N, adj_list
        self.edges = edges
        
        # Since it must be the distance FROM node1 or FROM node2, we can simply
        # run a bfs from EACH of these two nodes! Then out of all the nodes they
        # can both visit, we'll take the one whose max of distances is minimized.

        # Step 1: Run BFS from node1
        # Since there's only at most one outgoing edge, keep going until edges[i] == -1 !
        d1 = self.getNodeDists(node1)
        d2 = self.getNodeDists(node2)

        best_node, best_cost = -1, float("inf")
        for i in range(N):
            cost = max(d1[i], d2[i])
            if cost < best_cost:
                best_cost = cost
                best_node = i
        return best_node

    
    def getNodeDists(self, node):
        edges = self.edges
        N = len(edges)

        res = [float("inf")] * N
        visited = set([-1])
        dist = 0
        while node not in visited:
            visited.add(node)
            res[node] = dist
            node = edges[node]
            dist += 1

        return res
        
    
    # def bfs(self, source_node):
    #     N, adj_list = self.N, self.adj_list

    #     d = defaultdict(lambda: float("inf"))
    #     queue = collections.deque([(source_node, 0)]) # (node, dist)
    #     visited = set([source_node])

    #     while queue:
    #         node, dist = queue.popleft()

    #         if dist < d[node]:
    #             d[node] = dist
            
    #         for neigh in self.adj_list[node]:



