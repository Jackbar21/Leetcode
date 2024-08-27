class Solution:
    def __init__(self):
        self.n = None
        self.directed_edges = {} # Edge to ln weights (mapped from succProb)
        self.prev = None
        self.end_node = None
        self.adj_list = None
    def dijkstra(self, s):
        # Dictionary mapping of shortest path (from s) for each node
        d = {
            i: float("inf") for i in range(self.n)
        }
        d[s] = 0

        min_heap = [(0, s)]
        for i in range(self.n):
            if i == s:
                continue
            min_heap.append((float("inf"), i))

        self.prev = {
            i: None for i in range(self.n)
        }
        self.prev[s] = s

        visited = set()
        while len(visited) < self.n:
            # Want to pop node with HIGHEST d-value that is NOT in visited
            best_val, best_node = heapq.heappop(min_heap)
            # Min heap will have at most n + m <= 3n elements inside
            # of it at any given point in time. So the complexity will
            # still be O((n+m)logn) = O(nlogn) [since m <= 2n], similar
            # to the classical heap implementation of dijkstra with only
            # at most n elements (without visited set) and frequent calls
            # CHANGE-KEY (i.e. changing priority level of element in heap).
            while best_node in visited:
                best_val, best_node = heapq.heappop(min_heap)
            
            # We only care about shortest path from s to self.end_node.
            # So if we've computed the result ALREADY for self.end_node
            # in d, then simply return d prematurely.
            if best_node == self.end_node:
                return d

            visited.add(best_node)
            for v, prob in self.adj_list[best_node]:
                u = best_node
                # s --> best_node
                # just "popped" best_node (== u)
                # and for each edge (u, v) from adj_list:
                # want s --> v to be min(s --> v, s --> u + cost(u,v)), 
                #       where cost(u,v) is computed using "log trick"

                # d[v] = min(d[v], d[u] + self.directed_edges[(u,v)])
                mapped_prob = -math.log(prob)
                new_cost = d[u] + mapped_prob
                if new_cost < d[v]:
                    d[v] = new_cost
                    self.prev[v] = u
                
                    # When we get to v in some future iteration (if not yet seen),
                    # the nice property is that even if there are many entries for
                    # node v in the heap, by property of min heaps, only the best
                    # (i.e. smallest) found candidate for v will be considered, and
                    # thus this algorithm will still be correct & optimal.
                    if v not in visited:
                        heapq.heappush(min_heap, (d[v], v))

        return d

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        self.n = n
        self.end_node = end_node
        assert len(edges) == len(succProb)
        # Idea: Leverage something like Dijkstra's (that returns smallest path where cost of
        # a path is defined as SUM of its edges) by changing the value of each edge to the LOG
        # of its value. This way, we can leverage properties of the log function, namely that
        # log(X) + log(Y) = log(XY) for any X,Y>0, and that X > Y > 0 ==> log(X) > log(Y).

        # Step 1: Graph reduction (change edge values, *as well as make graph directed)
        # math.log from python is in base e (== 2.718281828...)
        # reduced_edges = [math.log(edge) for edge in edges]

        # Create adjaceny list of graph for faster edge population
        # traversals inside dijkstra's algorithm call. We can afford
        # this computation below efficiently since m is bounded by 2 * n :)
        self.adj_list = { i: [] for i in range(self.n) }
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            mapped_prob = -math.log(prob)

            self.adj_list[u].append((v, prob))
            self.adj_list[v].append((u, prob))
        
        # Naive array implementation: O(n^2)
        # Heap implementation: O((n+m)logn) = O(nlogn) [since m <= 2n]
        d = self.dijkstra(start_node)

        # Now we have access to self.prev, which gives us the previous node
        # in the shortest path with source node s to any destination node.
        # So, traverse from end_node backwards to start_node, get the probability
        # edge weights from succProb, and return the product of those probabilities.
        # But first, if there is no path from start_node to end_node, return 0.
        if self.prev[end_node] == None:
            return 0
        
        # O(n)
        probs = {}
        for i in range(len(edges)):
            u, v = edges[i]
            probs[(u, v)] = succProb[i]
            probs[(v, u)] = succProb[i]
        
        # O(n) work
        res_prob = 1
        cur_node = end_node
        while cur_node != start_node:
            prev_node = self.prev[cur_node]
            res_prob *= probs[(prev_node, cur_node)]
            cur_node = prev_node
        
        return res_prob

