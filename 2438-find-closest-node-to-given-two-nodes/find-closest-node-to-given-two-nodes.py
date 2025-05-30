class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        # Since it must be the distance FROM node1 or FROM node2, we can simply
        # run a bfs from EACH of these two nodes! Then out of all the nodes they
        # can both visit, we'll take the one whose max of distances is minimized.

        # Run BFS from node1 & node2
        # Since there's only at most one outgoing edge, keep going until edges[i] == -1 !
        def getNodeDists(node):
            res = [float("inf")] * N
            visited = set([-1])
            dist = 0
            while node not in visited:
                visited.add(node)
                res[node] = dist
                node = edges[node]
                dist += 1
            return res

        d1 = getNodeDists(node1)
        d2 = getNodeDists(node2)

        best_node, best_cost = -1, float("inf")
        for i in range(N):
            dist1, dist2 = d1[i], d2[i]
            cost = dist1 if dist1 > dist2 else dist2
            if cost < best_cost:
                best_cost = cost
                best_node = i

        return best_node
