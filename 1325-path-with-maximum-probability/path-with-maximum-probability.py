class Solution:
    def __init__(self):
        self.n = None
        self.edges = None
        self.succProb = None
        self.directed_edges = {} # Edge to ln weights (mapped from succProb)
        self.prev = None
        self.end_node = None
    def dijkstra(self, s):
        # Dictionary mapping of shortest path (from s) for each node
        d = [0] * self.n
        d[s] = 1
        # min_heap = [(d[i], i) for i in range(self.n)]
        # heapq.heapify(min_heap) # O(n)
        # node_to_index = {s: 0}
        # Simulate max_heap by using internal python heapq min-heap, and multiplying
        # all values by negative 1.

        max_heap = [(-1, s)]
        for i in range(self.n):
            if i == s:
                continue
            max_heap.append((0, i))


        visited = set()

        while len(visited) < self.n:
        # while len(min_heap) > 0:
        # while self.end_node not in visited:
            # Want to pop node with HIGHEST d-value that is NOT in visited
            best_prob, best_node = heapq.heappop(max_heap)
            best_prob = -best_prob
            # Min heap will have at most n + m <= 3n elements inside
            # of it at any given point in time. So the complexity will
            # still be O((n+m)logn) = O(nlogn) [since m <= 2n], similar
            # to the classical heap implementation of dijkstra with only
            # at most n elements (without visited set) and frequent calls
            # CHANGE-KEY (i.e. changing priority level of element in heap).
            while best_node in visited:
                best_prob, best_node = heapq.heappop(max_heap)
                best_prob = -best_prob
            
            # We only care about shortest path from s to self.end_node.
            # So if we've computed the result ALREADY for self.end_node
            # in d, then simply return d prematurely.
            if best_node == self.end_node:
                return d

            visited.add(best_node)
            # for u, v in self.directed_edges:
            # for u, v in self.edges:
            for i in range(len(self.edges)):
                u, v = self.edges[i]
                # Hacky trick for now...
                if v == best_node:
                    u, v = v, u
                if u == best_node:
                    # s --> best_node
                    # just "popped" best_node (== u)
                    # and for each edge (u, v)
                    # then want s --> v to be min(s --> v, s --> u + cost(u,v))

                    # d[v] = min(d[v], d[u] + self.directed_edges[(u,v)])
                    # mapped_val = float("inf") if self.succProb[i] == 0 else -math.log(self.succProb[i])
                    # mapped_val = -math.log(self.succProb[i])
                    # new_cost = d[u] + self.directed_edges[(u,v)]
                    # new_cost = d[u] + mapped_val

                    # UPDATE: 
                    # new_cost instead of being:
                    #        min(s --> v, s --> u + cost(u,v)) ; with -log trick
                    # will now be:
                    #        max(s --> v, s --> u * prob(u,v))
                    new_cost = d[u] * self.succProb[i]

                    # if new_cost < d[v]:
                    if new_cost > d[v]:
                        d[v] = new_cost
                        # self.prev[v] = u
                    
                        # When we get to v in some future iteration (if not yet seen),
                        # the nice property is that even if there are many entries for
                        # node v in the heap, by property of min heaps, only the best
                        # (i.e. smallest) found candidate for v will be considered, and
                        # thus this algorithm will still be correct & optimal.
                        if v not in visited:
                            heapq.heappush(max_heap, (-d[v], v))

        return d

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        start, end = start_node, end_node
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)]    
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:

                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        return 0.0
        self.n = n
        self.edges = edges
        self.succProb = succProb
        self.end_node = end_node
        assert len(edges) == len(succProb)
        # Idea: Leverage something like Dijkstra's (that returns smallest path where cost of
        # a path is defined as SUM of its edges) by changing the value of each edge to the LOG
        # of its value. This way, we can leverage properties of the log function, namely that
        # log(X) + log(Y) = log(XY) for any X,Y>0, and that X > Y > 0 ==> log(X) > log(Y).

        # Step 1: Graph reduction (change edge values, *as well as make graph directed)
        # math.log from python is in base e (== 2.718281828...)
        # reduced_edges = [math.log(edge) for edge in edges]

        # Populate directed_edges with costs from ln_edges
        # for i in range(len(edges)):
        #     u, v = edges[i]
        #     # Negative natural log mapping of succProb[i] value
        #     mapped_val = -math.log(succProb[i])
        #     self.directed_edges[(u,v)] = mapped_val
        #     self.directed_edges[(v,u)] = mapped_val
        
        # Naive array implementation: O(n^2)
        # Heap implementation: O((n+m)logn) = O(nlogn) [since m <= 2n]
        d = self.dijkstra(start_node)
        return d[self.end_node]

        # Now we have access to self.prev, which gives us the previous node
        # in the shortest path with source node s to any destination node.
        # So, traverse from end_node backwards to start_node, get the probability
        # edge weights from succProb, and return the product of those probabilities.
        

        # If there is no path from start_node to end_node, return 0
        # if self.prev[end_node] == None:
        #     return 0
        
        # # O(n)
        # probs = {}
        # for i in range(len(edges)):
        #     u, v = edges[i]
        #     probs[(u, v)] = succProb[i]
        #     # probs[(v, u)] = succProb[i]
        
        # # O(n) work
        # res_prob = 1
        # cur_node = end_node
        # while cur_node != start_node:
        #     prev_node = self.prev[cur_node]
        #     if (prev_node, cur_node) in probs:
        #         res_prob *= probs[(prev_node, cur_node)]
        #     else:
        #         assert (cur_node, prev_node) in probs
        #         res_prob *= probs[(cur_node, prev_node)]
        #     cur_node = prev_node
        
        # return res_prob

