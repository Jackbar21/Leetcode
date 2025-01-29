class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        # Idea: Loop through all the edges in reversed order (since if multiple answers,
        # problem statement says to return one that occurs last in the input). Then for
        # each considered edge, delete that edge, and check if the graph is STILL just
        # one strongly connected component via a simple DFS, starting from any node
        # (since the graph is undirected!). Then that edge didn't work, add it back,
        # and try with the next one, until a valid / 'redundant' one is found :)

        # Step 1: Build an adjacency list (via sets to allow O(1) edge deletion & insertion!)
        adj_list = [set() for _ in range(N + 1)] # Since nodes labeled 1 to N :)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        # Step 2: Loop through edges in backwards order, until first redundant one is found!
        for u, v in reversed(edges):
            # Delete the edge
            adj_list[u].remove(v)
            adj_list[v].remove(u)

            # Run DFS from any node and check if can reach every other node (which would mean
            # the deleted edge was redundant!).
            # TODO: Don't make this random/fixed, be greedy!
            random_node = u

            visited = set([random_node])
            stack = [random_node]
            while len(stack) > 0:
                node = stack.pop()
                for neigh in adj_list[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    stack.append(neigh)
            
            if len(visited) == N:
                return (u, v)

            # Add the edge (since it wasn't redundant!)
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        raise Exception("Unreachable Code - There must be a solution!")
