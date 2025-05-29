class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N, M = len(edges1) + 1, len(edges2) + 1

        adj_list1 = [[] for _ in range(N)]
        indegree1 = [0] * N
        for a, b in edges1:
            adj_list1[a].append(b)
            adj_list1[b].append(a)
            indegree1[a] += 1
            indegree1[b] += 1
        
        adj_list2 = [[] for _ in range(M)]
        indegree2 = [0] * M
        for u, v in edges2:
            adj_list2[u].append(v)
            adj_list2[v].append(u)
            indegree2[u] += 1
            indegree2[v] += 1
        
        # Make the root node of each tree the one with SMALLEST indegree!
        def getNodeWithSmallestIndegree(node_count, indegree):
            root, degree = None, float("inf")
            for node in range(node_count):
                if indegree[node] < degree:
                    root = node
                    degree = indegree[node]
            assert root is not None
            return root

        # After coding this up, I now realize I can just make ANY node the root...
        # root1 = getNodeWithSmallestIndegree(N, indegree1)
        # root2 = getNodeWithSmallestIndegree(M, indegree2)
        # print(f"{root1=}")
        # print(f"{root2=}")
        # So let's just make 0 the root every time for easier testing
        root1 = root2 = 0
        
        # Now, for each node, we shall compute its DEPTH. This will be relevant
        # for dictating whether two nodes are EVEN or ODD reachability apart!
        def getNodeDepths(root, node_count, adj_list):
            res = [None] * node_count
            queue = collections.deque([(root, 0)]) # (node, depth)
            visited = set([root])
            while queue:
                node, depth = queue.popleft()

                assert res[node] is None
                res[node] = depth

                for neigh in adj_list[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    queue.append((neigh, depth + 1))
            
            assert None not in res
            return res

        depth1 = getNodeDepths(root1, N, adj_list1)
        depth2 = getNodeDepths(root2, M, adj_list2)

        # Now, the idea is that nodes at an EVEN depth, or EVEN distance away from other
        # nodes at EVEN depths, and ODD distance away from other nodes at ODD depths.
        # This is similar for nodes at ODD depths.

        # print(f"{depth1=}")
        # print(f"{depth2=}")
        sum_even1 = sum(depth1[i] % 2 == 0 for i in range(N))
        sum_odd1 = sum(depth1[i] % 2 == 1 for i in range(N))

        sum_even2 = sum(depth2[i] % 2 == 0 for i in range(M))
        sum_odd2 = sum(depth2[i] % 2 == 1 for i in range(M))

        # print()
        # print(f"{sum_even1=}")
        # print(f"{sum_odd1=}")
        # print()
        # print(f"{sum_even2=}")
        # print(f"{sum_odd2=}")

        # So then, using same trick as in attempt below, we can take max of `sum_even2`
        # and `sum_odd2` and slap it to reachability of every node in tree 1. This is
        # because we can choose to either add an edge from node i or a node 1 distance
        # away from i (a neighbor) to greedily pick odd OR even reachability nodes in the 
        # second tree.
        max_reachability = max(sum_even2, sum_odd2)

        # For each node in the first tree, we will want all the ones that are
        # EVEN reachable away from that node. Moreover, all the nodes that share
        # the same parity in DEPTH level (i.e. even depth -> other even depth nodes,
        # and similarly for odd depth nodes.)
        res = []
        for node in range(N):
            is_even_depth = depth1[node] % 2 == 0
            reachability = sum_even1 if is_even_depth else sum_odd1
            res.append(reachability + max_reachability)
        return res

    def maxTargetNodesAttempt(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # This is my first attempt at solving this problem, it does so CORRECTLY but inefficiently.
        # It follows spirit similar in nature to my solution to Part I of this Leetcode problem.
        N, M = len(edges1) + 1, len(edges2) + 1

        adj_list1 = [[] for _ in range(N)]
        for a, b in edges1:
            adj_list1[a].append(b)
            adj_list1[b].append(a)
        
        adj_list2 = [[] for _ in range(M)]
        for u, v in edges2:
            adj_list2[u].append(v)
            adj_list2[v].append(u)
        
        # Since we must apply the operation for every node i, 0 <= i < N, in the first tree--
        # Let i be arbitrary.
        # The idea, is that since there's AT LEAST TWO nodes in the first tree, namely that N >= 2,
        # we can choose to either:
        #
        #   (1) Connect an edge from node i to another node i' in second tree, leaving us with
        #       all nodes that are an ODD reachability away from node i' in the second tree
        #
        #   (2) Connect an edge from a node that is a distance of 1 away from node i to another
        #       node i' in second tree, leaving us with all nodes that are an EVEN reachability
        #       away from node i' in the second tree
        assert N >= 2

        # What this therefore allows us to do, is to greedily select the highest ODD/EVEN reachability
        # of ANY node in the second tree, as we can leverage this result in a similar way to how
        # we leveraged the "maximum k-1 reachable node" in part I of this Leetcode problem!
        max_reachability = max(
            max(self.getOddReachabilityCounts(M, adj_list2)),
            max(self.getEvenReachabilityCounts(M, adj_list2))
        )

        # Now, for each node i in the first tree, we can simply connect an edge from node i
        # or a node that is 1 away from node i to obtain the maximum reachability count from
        # the second tree--namely the variable `max_reachability` computed above.
        # Since we are specifically interested in EVEN distances, we will add each node's
        # even reachability count from the first tree and the maximum reachability (odd OR even)
        # of any node in the second tree. This is in similar spirit to part I of this Leetcode problem!
        even_reachability_counts = self.getEvenReachabilityCounts(N, adj_list1)
        return [reachability + max_reachability for reachability in even_reachability_counts]
        
    def getOddReachabilityCounts(self, node_count, adj_list):
        return self.getReachabilityCounts(node_count, adj_list, True)
    
    def getEvenReachabilityCounts(self, node_count, adj_list):
        return self.getReachabilityCounts(node_count, adj_list, False)
    
    def getReachabilityCounts(self, node_count, adj_list, is_odd):
        # Returns a list of size `node_count` where the i'th index represents
        # how many nodes are reachable from the i'th node that are an ODD distance away!
        
        res = []
        for i in range(node_count):
            queue = collections.deque([(i, 0)]) # (node, path_len)
            visited = set([i])
            reachability_count = 0
            while queue:
                node, path_len = queue.popleft()
                parity = path_len % 2

                if is_odd and parity == 1:
                    reachability_count += 1
                elif (not is_odd) and parity == 0:
                    reachability_count += 1
                
                for neigh in adj_list[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    queue.append((neigh, path_len + 1))

            res.append(reachability_count)
        
        return res
