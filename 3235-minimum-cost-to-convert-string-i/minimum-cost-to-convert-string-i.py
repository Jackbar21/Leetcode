class Solution:
    def __init__(self):
        self.nodes = None
        self.edges = None
    def dijkstra(self, s):
        # Naive with array: O(n^2)
        # With heap: O((n+n)logn), where m = len(edges), n = len(nodes)
        # BUT, m <= n in this problem, so heap version wins!!

        # PSEUDOCODE:
        # R := \empty
        # d(s) := 0 ; p(s) := NIL
        # for each v != s do d(v) := INF ; p(v) = NIL
        # while R != V do
        #   let u be node NOT in R with min d-value
        #   R := R U {u}
        #   for each v s.t. (u,v) \in E do:
        #       if d(v) > d(u) + wt(u,v) then
        #           d(v) := d(u) + wt(u,v) ; p(v) := u
        d = {
            node: float('inf') for node in self.nodes
        }
        d[s] = 0

        visited = set()
        while len(visited) < len(self.nodes):
            # TODO: below can be optimized using min-heap instead...
            # O(logn) instead of O(n)
            u, d_u = None, float("inf")
            for node in d:
                if node not in visited and d[node] <= d_u:
                    u, d_u = node, d[node]
            visited.add(u)

            for v in self.nodes:
                if (u, v) in self.edges:
                    d[v] = min(d[v], d_u + self.edges[(u,v)])
            
        return d

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if len(source) != len(target):
            return -1

        nodes = set([letter for letter in 'abcdefghijklmnopqrstuvwxyz'])
        
        assert len(original) == len(changed) == len(cost)
        edges = {} # {(u,v): c} for every edge u -> v with cost c
        for i in range(len(original)):
            o, c = original[i], changed[i]
            cst = min(
                edges.get((o,c), float("inf")),
                cost[i]
            )
            edges[(o, c)] = cst
        self.nodes, self.edges = nodes, edges
        
        total = 0
        dijkstra_mappings = {}
        assert len(source) == len(target)
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            
            if source[i] not in dijkstra_mappings:
                dijkstra_mappings[source[i]] = self.dijkstra(source[i])
            
            d = dijkstra_mappings[source[i]]
            assert target[i] in d
            if d[target[i]] == float('inf'):
                return -1
            total += d[target[i]]
        
        return total
