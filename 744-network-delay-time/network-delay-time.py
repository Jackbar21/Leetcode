class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Idea: Traverse the graph until reaching every node, but using an algorithm
        # like UCS or Dijkstra's instead of BFS (since edges aren't necessarily equal!)
        # I will use UCS, since it is simpler :)

        # Step 1: Build adjacency list (with weights!)
        adj_list = [set() for _ in range(n + 1)]
        for u, v, w in times:
            adj_list[u].add((v, w)) # (neigh, weight)

        # Step 2: Traverse the graph using UCS, and get total time to reach all nodes
        # as quickly as possible!
        res = 0
        fringe = [(0, k)] # (time, node) -- min heap for UCS!
        visited = set()
        while len(fringe) > 0 and len(visited) < n:
            time, node = heapq.heappop(fringe)

            # If already visited a node, already found shortest path to it!
            if node in visited:
                continue
            visited.add(node)

            # Minimum time will only be as fast as bottleneck in the network!
            # "The chain is only as strong as that of the weakest link!"
            if time > res:
                res = time

            for neigh, w in adj_list[node]:
                # If neigh already in visited, then already
                # found minimal cost to reach neigh from k :)
                if neigh not in visited:
                    heapq.heappush(fringe, (time + w, neigh))

        return res if len(visited) == n else -1
