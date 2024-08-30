class Solution:
    def __init__(self):
        self.adj_list = None # a_i: [b_i, ...]
        self.edge_costs = None # {(a_i,b_i): w_i, ...}
        self.n = None # n
        self.source = None # source
        self.dest = None # destination
        self.banned_mod_edges = set() # edges banned from modification in other paths
        self.modifiable_edges = set() # edges with initial weight of -1
        self.banned_paths = set() # paths that we tried setting to cost target, but no sol'n found
    def get_edge_cost(self, edge):
        return self.edge_costs[edge]
    def ban_mod_edge(self, edge):
        u, v = edge
        assert (u, v) in self.modifiable_edges
        assert (v, u) in self.modifiable_edges
        assert (u, v) not in self.banned_mod_edges
        assert (v, u) not in self.banned_mod_edges

        self.modifiable_edges.remove((u, v))
        self.modifiable_edges.remove((v, u))
        self.banned_mod_edges.add((u, v))
        self.banned_mod_edges.add((v, u))
    def unban_mod_edges(self):
        for edge in self.banned_mod_edges:
            assert edge not in self.modifiable_edges
            self.modifiable_edges.add(edge)
        self.banned_mod_edges.clear()
    def reset_mod_edges(self):
        self.unban_mod_edges()
        self.set_mod_edges(1)
    def set_mod_edges(self, value):
        for edge in self.modifiable_edges:
            self.set_edge_cost(edge, value)
    def set_banned_mod_edges(self, value):
        for edge in self.banned_mod_edges:
            self.set_edge_cost(edge, value)
    def get_current_edges(self):
        ignore_edges = set()
        edges = []
        for edge in self.edge_costs:
            if edge in ignore_edges:
                continue
            
            u, v = edge
            cost = self.edge_costs[edge]
            ignore_edges.add((v, u))
            edges.append([u, v, cost])

        return edges
    def set_edge_cost(self, edge, new_cost):
        u, v = edge
        self.edge_costs[(u, v)] = new_cost
        self.edge_costs[(v, u)] = new_cost
        return
    def dijkstra(self, s):
        # Naive array implementation: O(n^2)
        # Heap implementation: O((n+m)logn) --> better when m = O(n)
        #     since m == edges.length <= n * (n - 1) / 2, m = O(n^2)
        #     therefore, Naive array implementation is BETTER!
        # But, for the 

        d = {
            i: float("inf") for i in range(self.n)
        }
        d[s] = 0
        visited = set()
        heap = [(0, s)] + [(float("inf"), i) for i in range(self.n) if i != s]
        prev = {
            i: None for i in range(self.n)
        }
        # heapq.heapify(heap) # O(n)

        while len(visited) < self.n:
            # assert len(heap) > 0
            # weight, node = heapq.heappop(heap)
            # if node in visited:
            #     continue
            
            # # We popped 'node'. Call this node 'u'.
            # # We now have shortest path of cost 'weight' from s ----> u.
            # u = node
            # d[u] = weight
            # visited.add(u)
            best_val, best_node = float("inf"), None
            for node in d:
                if node in visited:
                    continue
                if d[node] <= best_val:
                    best_val = d[node]
                    best_node = node
            u = best_node
            assert d[u] == best_val
            visited.add(u)

            # For every edge (u,v), we can then say that:
            #   shortest s ----> v path is either:
            #       (1) s ----> v, OR
            #       (2) s ----> u  +  cost(u, v)
            for v in self.adj_list[u]:
                cost = self.edge_costs[(u,v)]
                if d[u] + cost < d[v]:
                    assert v not in visited
                    d[v] = d[u] + cost
                    prev[v] = u
                    # heapq.heappush(heap, (d[v], v))
        
        return (d, prev)
    def get_shortest_path(self, prev):
        # PRE-CONDITION: self.banned_mod_edges must be empty
        assert len(self.banned_mod_edges) == 0

        shortest_path = collections.deque()
        cur_node = self.dest
        while cur_node != self.source:
            prev_node = prev[cur_node]
            assert prev_node is not None
            edge = (prev_node, cur_node)
            shortest_path.appendleft(edge)
            if edge in self.modifiable_edges:
                self.ban_mod_edge(edge)

            # Loop Invariant
            cur_node = prev_node
        
        return tuple(shortest_path)
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        self.n, self.source, self.dest = n, source, destination
        self.adj_list = {
            i: [] for i in range(self.n)
        }

        self.edge_costs = {}
        for (u,v,cost) in edges:
            # (u,v,cost) <--> (a,b,w)
            # self.adj_list[u].append((v, cost))
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
            if cost == -1:
                self.modifiable_edges.add((u,v))
                self.modifiable_edges.add((v,u))
                cost = 1
            self.edge_costs[(u,v)] = cost
            self.edge_costs[(v,u)] = cost
        
        # Problem setup finished!
        # Defined tools & helpers:
        #       (1) self.dijkstra(s)
        #       (2) self.set_edge_cost(edge, new_cost)
        #       (3) self.edge_costs --> modifiable edge costs
        #       (4) self.modifiable_edges --> constant set of all modifiable edges
        d, prev = self.dijkstra(self.source)
        assert prev[self.dest] is not None

        # Get shortest path, and set of modifiable
        # edges in that path
        # cur_node = self.dest
        # while cur_node != self.source:
        #     prev_node = prev[cur_node]
        #     assert prev_node is not None
        #     edge = (prev_node, cur_node)
        #     shortest_path.appendleft(edge)
        #     if edge in self.modifiable_edges:
        #         # self.banned_mod_edges.add(edge)
        #         self.ban_mod_edge(edge)
        #     # Loop Invariant
        #     cur_node = prev_node
        shortest_path = self.get_shortest_path(prev)
        
        # Base Case #1: Shortest path doesn't contain any modifiable
        # edges, and cost is not equal to target. Therefore, we can
        # NEVER modify the modifiable edges in such a way where the
        # shortest path from source to destination becomes target.
        if len(self.banned_mod_edges) == 0 and d[self.dest] != target:
            return []
        
        # Base Case #2: Since all modifiable edges are currently set to their 
        # MINIMUM value of 1, we can only make every path BIGGER. So if current
        # shortest path is GREATER than target, we will never be able to
        # make it smaller, and hence we return an empty array.
        if d[self.dest] > target:
            return []

        # Base Case #3: If shortest path is ALREADY equal to target, just return
        # the edges already!
        if d[self.dest] == target:
            return self.get_current_edges()

        # Problem setup & Base Case check finished!
        # Reminder of defined tools & helpers:
        #       (1) self.dijkstra(s)
        #       (2) self.set_edge_cost(edge, new_cost)
        #       (3) self.edge_costs --> modifiable edge costs
        #       (4) self.modifiable_edges --> constant set of all modifiable edges
        assert d[self.dest] < target
        assert len(self.banned_mod_edges) > 0

        # Idea: We will modify the edges in 'self.banned_mod_edges' to make
        # the cost of this found shortest path equal to target.
        # Since we know that in order to solve the problem, we
        # just need AT LEAST ONE shortest path of cost target
        # (can be more than one, but just one also SUFFICES),
        # we can "blow up" the values of ALL other modifiable
        # edges to be equal to target, and that way we now have
        # the original shortest path equal to target, and all
        # other paths be >= target IF it was the case that they
        # COULD have been made equal to target. That way, we may
        # simply just run dijkstra's algorithm again, in which
        # case we simply check if the now-shortest path is equal
        # to target, and return the current set of edges if so.
        # Otherwise, of course, we simply return [] as there is
        # no solution.
        #
        # Alternative explanation: we found the original shortest path,
        # and now we will set its value to target. Then for EVERY
        # other modifiable path, i.e. a path with modifiable edge(s)
        # that DO NOT belong to the set of modifiable edges in the
        # currently found shortest path (since modifying any of those
        # would augment the cost of the path with value target), we
        # set its value to target so that the cost of the full path
        # necessarily becomes >= target, by the fact that ALL edges
        # are positive in weight. And henceforth, if the shortest path
        # then becomes less than target, it's because there exists a
        # no-longer editable path from source to destination, in which
        # case we simply return [].

        while shortest_path not in self.banned_paths:

            # Step 1: Modify weight of current shortest path to be equal to target
            # We can do this by taking literally any edge in self.banned_mod_edges, and adding
            # to its cost the missing difference between current shortest path and target.
            missing_difference = target - d[self.dest]
            assert missing_difference > 0
            if len(self.banned_mod_edges) == 0:
                return []
            edge = self.banned_mod_edges.pop() # *** Remember to add this BACK IN afterwards!
            cost = self.get_edge_cost(edge)
            assert cost == 1 # sanity check to boost confidence in reset function calls later on
            self.set_edge_cost(edge, cost + missing_difference)
            self.banned_mod_edges.add(edge)

            # Step 2: Modify all other modifiable edges to be equal to target
            # print(self.get_current_edges())
            # print(f"{self.banned_mod_edges=}, {self.modifiable_edges=}")
            # for edge in self.modifiable_edges:
            #     u, v = edge
            #     if (u, v) not in self.banned_mod_edges and (v, u) not in self.banned_mod_edges:
            #         print(f"MODIFYING: {edge}")
            #         self.set_edge_cost(edge, target)
            self.set_mod_edges(target)


            new_d, new_prev = self.dijkstra(self.source)
            # print(new_d)
            cur_edges = self.get_current_edges()
            # print(cur_edges)
            assert new_d[self.dest] <= target
            if new_d[self.dest] == target:
                return cur_edges
            # else:
            self.banned_paths.add(shortest_path)
            self.reset_mod_edges()
            new_shortest_path = self.get_shortest_path(new_prev)
            # if new_shortest_path in self.banned_paths:
            #     return []

            # Loop Invariant
            d, prev, shortest_path = new_d, new_prev, new_shortest_path
            
            # print("GIGA!!")
            # print(self.banned_mod_edges)
            # print(self.modifiable_edges)
        
        return []    





        # Our idea didn't work. There's two possible cases:
        # (1) at least one of the other paths are not editable,
        #     AND the cost of the path is less than target, 
        #     in which case there IS NO SOLUTION... OR
        # (2) There exists a solution where the original shortest
        #     path is GREATER than target but NEVER when EQUAL to target

        # EDIT: I'm realizing that case (1) is actually NOT POSSIBLE
        # We essentially have to keep trying other paths, until we've
        # exhausted them all (which nevermind - maybe case 1 is true?)

        

        # step 2 additional commentary...:
        #    with the rationaly behind this being to set all other editable paths
        #         to have total path cost >= target, with at least our initial
        #         shortest path having value of target.