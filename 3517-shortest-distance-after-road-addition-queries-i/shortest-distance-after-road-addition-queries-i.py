class Solution:
    def __init__(self):
        self.shortest_paths = {} # (s,t): cost
    def getShortestPath(self, s, t):
        return self.shortest_paths.get((s, t), t - s)
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Idea: get shortest path from 0 to s for every s, 1 <= s <= n - 1.
        # Whenever a new edge from u to v gets added, take the current cost from 0 to u,
        # and bfs from node u, and changing the cost of the shortest path to any found
        # node t in the bfs search as the minimum between shortest & current path costs.

        # For now, let's code up the trivial way to do this problem (call bfs from 0
        # after each query)
        adj_list = {i: set() for i in range(n)}
        for i in range(n - 1):
            u, v = i, i + 1
            adj_list[u].add(v)
            # adj_list[v].add(u)
        
        answer = []
        for (u, v) in queries:
            adj_list[u].add(v)
            # adj_list[v].add(u)
            answer.append(self.getShortestPath(adj_list, 0, n - 1))
        
        print(adj_list)
        return answer
        
    
    def getShortestPath(self, adj_list, s, t):
        queue = collections.deque([(s, 0, "0")]) # (node, cost, path)
        visited = set([s])
        while len(queue) > 0:
            node, cost, path = queue.popleft()
            if node == t:
                print(f"{path=}")
                return cost

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, cost + 1, f"{path} -> {neighbor}"))
        
        return float("inf")
            
        
        # answer = []
        # for query in queries:
        #     u, v = query
        #     assert u < v
        #     self.shortest_paths((u, v)) = 
        
