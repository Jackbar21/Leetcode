class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        # We're going to apply the same operation for every node i, 0 <= i < n, in the first tree.
        # Hence, let i be arbitrary.
        # 
        # Since we're able to add an edge from i to some other arbitrary node i' in the second tree,
        # we can simply connect it to the node in the second tree that has the maximal amount of
        # target nodes with value k - 1 (since one out of k edges is reserved from i to i').
        # We can do this computation once in O(m^2) time in the second tree, and use it for
        # every node in the first tree.
        N, M = len(edges1) + 1, len(edges2) + 1

        adj_list1 = [[] for _ in range(N)]
        for a, b in edges1:
            adj_list1[a].append(b)
            adj_list1[b].append(a)

        adj_list2 = [[] for _ in range(M)]
        for u, v in edges2:
            adj_list2[u].append(v)
            adj_list2[v].append(u)

        # Step 1: Get node in second tree with maximal number of target nodes with value k - 1.
        max_reachability = max(self.getNodeReachabilities(M, adj_list2, k - 1))

        # Step 2: For each node in first tree, figure out its reachability 
        reachable = self.getNodeReachabilities(N, adj_list1, k)

        # Step 3: Add max reachability to each node in tree1's already set reachability!
        return [reachability + max_reachability for reachability in reachable]

    def getNodeReachabilities(self, node_count, adj_list, max_distance):
        if max_distance == 0:
            return [1] * node_count # Just the node itself!
        elif max_distance < 0:
            return [0] * node_count # No nodes to reach, not even itself!

        reachable = []
        for i in range(node_count):
            queue = collections.deque([(i, 0)])
            visited = set([i])
            while queue:
                node, distance = queue.popleft()

                # assert distance <= max_distance
                if distance == max_distance:
                    continue # No more exploration!
                
                for neigh in adj_list[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, distance + 1))
            
            reachable.append(len(visited))
        
        return reachable