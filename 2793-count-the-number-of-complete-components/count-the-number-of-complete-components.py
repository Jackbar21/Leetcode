class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        adj_list = {node: [] for node in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Step 2: Get all components
        components = []
        nodes = set(range(n))
        visited = set()
        while len(nodes) > 0:
            node = nodes.pop()
            if node in visited:
                # Already belongs to another connected components
                continue
            visited.add(node)
            
            # This is the beginning of a NEW connected component!
            component = [node]
            stack = [node] # dfs
            while len(stack) > 0:
                node = stack.pop()
                for neigh in adj_list[node]:
                    if neigh not in visited:
                        component.append(neigh)
                        stack.append(neigh)
                        visited.add(neigh)
            
            components.append(component)
        
        # Step 3: Count how many connected components are actually COMPLETE
        res = 0
        for component in components:
            # Say this component consists of N nodes. In order for it to be a
            # COMPLETE connected component, it must be that every pair of nodes
            # have an edge between one another. For this to be true, it must be
            # that EVERY NODE in this component has exactly N - 1 neighbors. 
            is_complete = True
            expected_neighbor_count = len(component) - 1
            for node in component:
                actual_neighbor_count = len(adj_list[node])
                if expected_neighbor_count != actual_neighbor_count:
                    is_complete = False
                    break
            res += is_complete

        return res


