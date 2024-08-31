class Solution:
    def __init__(self):
        self.adj_list = None
        self.n = None
    def dijkstra(self, s):
        # This is a special version of dijkstra, which returns the maximum-product
        # path instead of the minimum-sum path.
        d = {
            i: 0 for i in range(self.n)
        }
        d[s] = 1

        max_heap = [(-1, s)] + [(0, i) for i in range(self.n) if i != s]
        visited = set()

        while len(visited) < self.n:
            best_val, best_node = heapq.heappop(max_heap)
            if best_node in visited:
                continue
            
            # Since we're simulating a max heap using python's heapq min-heap
            # implementation by multiplying all the values by -1, we must make
            # sure to multiply by -1 again when we pop them from the heap (not just insert)
            u = best_node
            d[u] = -best_val
            visited.add(u)

            # We now have the BEST (maximum-product not minimum-sum) path from s to u,
            # s ---> u. Now for every edge (u,v), we want to update s ---> v to be the
            # better (in this case larger) between s ---> v and s ---> u (== d[u]) + cost(u,v)
            for v, prob in self.adj_list[u]:
                new_cost = d[u] * prob
                if new_cost > d[v]:
                    d[v] = new_cost
                    heapq.heappush(max_heap, (-new_cost, v)) # -new_cost since max-heap!
        
        return d




    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        self.n = n
        self.adj_list = {i: [] for i in range(self.n)}
        assert len(edges) == len(succProb)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            self.adj_list[u].append((v, prob))
            self.adj_list[v].append((u, prob))

        d = self.dijkstra(start_node)
        return d[end_node]
