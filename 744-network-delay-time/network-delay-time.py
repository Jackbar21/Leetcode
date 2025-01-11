class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Idea: Traverse the graph until reaching every node, but using an algorithm
        # like UCS or Dijkstra's instead of BFS (since edges aren't necessarily equal!)
        # I will use UCS, since it is simpler :)

        # Step 1: Build adjacency list (with weights!)
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w)) # (neigh, weight)

        # Step 2: Traverse the graph using UCS, and get total time to reach all nodes
        # as quickly as possible!
        res = 0
        fringe = [(0, k)] # (time, node) -- min heap for UCS!
        visited = set()
        while len(fringe) > 0:# and len(visited) < n:
            time, node = heapq.heappop(fringe)
            # if node in visited and node != k:
            #     continue
            if node in visited:
                continue
            else:
                visited.add(node)

            if time > res:
                res = time

            for neigh, w in adj_list[node]:
                if neigh in visited:
                    continue
                
                # visited.add(neigh)
                heapq.heappush(fringe, (time + w, neigh))

        return res if len(visited) == n else -1


# 1 --t=1--> 2 ---t=2---> 3
# |
# t=4
# |
# v
# 3