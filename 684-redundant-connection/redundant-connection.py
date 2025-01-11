class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # O(n^2)
        adj_list = []
        for u, v in edges:
            while len(adj_list) < max(u, v) + 1:
                adj_list.append(set())
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        # Since there are no repeated edges, and it is an UNDIRECTED graph,
        # length of adj_list must be the number of nodes IN graph (i.e. each
        # node is connected by at least ONE edge, and therefore in adj_list)
        N = len(adj_list) - 1

        # Try removing the last edge in edges, and everytime checking if the graph
        # forms a tree. We can check if the graph is a tree by picking a random node,
        # performing a dfs/bfs traversal from that node, and checking if every other
        # node was indeed reachable in the graph (in similar spirit to the "Number of 
        # Connected Components In An Undirected Graph" problem).
        for u, v in reversed(edges):
            # Step 1: Remove the edge
            adj_list[u].remove(v)
            adj_list[v].remove(u)

            # Step 2: Pick a random node, perform dfs, and return edge if forms tree!
            # node = random.randint(1, N)
            # Might as well not waste time calling 'random.randint' if can avoid it :p
            node = u if len(adj_list[u]) < len(adj_list[v]) else v
            stack = [node] # dfs
            visited = set([node])
            while len(stack) > 0:
                node = stack.pop()
                for neigh in adj_list[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        stack.append(neigh)
            if len(visited) == N:
                return (u, v)

            # Step 3: Add the edge back
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        raise Exception("No Solution")
