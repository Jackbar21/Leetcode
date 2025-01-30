class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Idea: Grab every connected component. If there is an odd cycle, return -1.
        # Otherwise, run a dfs from every node, and grab the length of the longest path.
        adj_list = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        res = 0

        # Nvm, just get every connected component. Then as you run a dfs/bfs from every node,
        # just make sure to watch out for odd length cycles!
        components = []
        unvisited = set(range(1, n + 1))
        while len(unvisited) > 0:
            node = unvisited.pop()
            visited = set([node])
            queue = collections.deque([node])
            while len(queue) > 0:
                node = queue.popleft()
                for neigh in adj_list[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    unvisited.remove(neigh)
                    queue.append(neigh)
            
            # Step 2: Run dfs from every node
            component = list(visited)
            components.append(component)

            max_path = 0
            for visited_node in component:
                visit_time = {visited_node: 0}
                queue = collections.deque([(0, visited_node)]) # (cur_time, node)
                while len(queue) > 0:
                    cur_time, node = queue.popleft()
                    max_path = max(max_path, cur_time + 1)

                    for neigh in adj_list[node]:
                        if neigh in visit_time:
                            # assert cur_time > visit_time[neigh]
                            if abs(cur_time + 1 - visit_time[neigh]) % 2 == 1:
                                print(f"{visited_node=}, {node=}, {cur_time=}, {neigh=}, {visit_time=}")
                                return -1 # Cannot have odd cycles!
                            continue
                        
                        visit_time[neigh] = cur_time + 1
                        queue.append((cur_time + 1, neigh))
            
            res += max_path

            
        for i, component in enumerate(components):
            print(f"components[{i}]={component}")

        return res

        # n = 500
        # print(f"{10**4}")
        # return n * (n+1)/2
        # Observation 1: If a node is at index k, ALL of its directly adjacent
        # neighbors must either be at index k-1 OR index k+1. 

        # Observation 2: We should probably but the node with SMALLEST degree
        # at the first index, although this is a GREEDY idea that may or may not work...

        # FACT: Any node that has no edges, essentially forms its own independent group
        # that we can shove to the end and forget about :)
        # for i in range(n):

        # FACT: I can solve this problem for each connected component, and take the sum
        # of the result for each component's maximum groupings!
        # for j in range(n):
        #     for k in range(n):
        #         pass
        
        return -1



        """
        G1 | G2 | G3 | G4
       ----|----|----|----
        3  | 2  | 1  | 5
           |    | 4  |
           |    | 6  |
           |    |    |
           |    |    |
     c   b | a  | d  |


                a -- d
              /        \
             b --- c -- e

        """

