class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        self.color = {i: colors[i] for i in range(N)}
        adj_list = {i: [] for i in range(N)}
        indegree = {i: 0 for i in range(N)}
        for a, b in edges:
            adj_list[a].append(b)
            indegree[b] += 1
        self.adj_list = adj_list
        self.memo = {}
        
        # Step 1: Detect if there's a cycle via topological sort
        queue = collections.deque(node for node in range(N) if indegree[node] == 0)
        topo_sort = []
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        # print(f"{topo_sort=}, {len(topo_sort)=}, {N=}")
        if len(topo_sort) < N:
            return -1 # Cycle detected!

        # Otherwise, search for best path!
        color_options = "abcdefghijklmnopqrstuvwxyz"
        return max(
            self.dp(node, color)
            for node in range(N)
            for color in color_options
        )

    def dp(self, node, color):
        if (node, color) in self.memo:
            return self.memo[(node, color)]

        val = 1 if self.color[node] == color else 0
        res = val
        for neigh in self.adj_list[node]:
            path_len = val + self.dp(neigh, color)
            if res < path_len:
                res = path_len
        
        self.memo[(node, color)] = res
        return res
