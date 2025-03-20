class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # G = (V, E), n = |V|, m = |E| (= len(edges))
        # BELLMAN-FORD: O(nm)
        # FLOYD-WARSHALL: O(n^3)
        # JOHNSON'S: O(mnlogn)
        # DP probably going to be too slow here... even though correct!

        # From constraints, we have that 0 <= w_i <= 10^5
        MAX_WEIGHT = pow(10, 5)
        MAX_BIT_COUNT = len(bin(MAX_WEIGHT)) - 2
        MAX_BITWISE_AND = int('1' * (MAX_BIT_COUNT), 2)

        adj_list = {node: [] for node in range(n)}
        for (u, v, w) in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        self.adj_list = adj_list

        nodes = set(range(n))
        visited = set()
        components = [] # (set_of_nodes, min_bitwise_and_cost)

        while len(nodes) > 0:
            node = nodes.pop()
            if node in visited:
                continue
            visited.add(node)
            
            # Perform bfs
            connected_component = set()
            bitwise_and = MAX_BITWISE_AND # only set bits as default!
            stack = [node]
            while len(stack) > 0:
                node = stack.pop()
                connected_component.add(node)

                for neigh, weight in self.adj_list[node]:
                    bitwise_and &= weight
                    if neigh not in visited:
                        stack.append(neigh)
                        visited.add(neigh)
            
            components.append((connected_component, bitwise_and))
        
        node_to_component = {}
        for component, bitwise_and in components:
            for node in component:
                assert node not in node_to_component
                node_to_component[node] = (component, bitwise_and)
        
        answer = []
        for s, t in query:
            component, bitwise_and = node_to_component[s]
            if t not in component:
                answer.append(-1)
                continue
            
            answer.append(bitwise_and)
        
        return answer

            
