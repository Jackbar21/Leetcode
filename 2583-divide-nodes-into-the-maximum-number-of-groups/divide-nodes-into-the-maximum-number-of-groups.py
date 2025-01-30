class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # FACT: I can solve this problem for each connected component, and take the sum
        # of the result for each component's maximum groupings!

        # Idea: Grab every connected component. If there is an odd cycle, return -1.
        # Otherwise, run a dfs from every node, and grab the length of the longest path.
        # Nvm, just get every connected component. Then as you run a dfs/bfs from every node,
        # just make sure to watch out for odd length cycles!

        # Step 1: Build adjacency list!
        adj_list = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        res = 0
        unvisited = set(range(1, n + 1))
        while len(unvisited) > 0:
            node = unvisited.pop()
            visited = set([node])
            stack = [node]
            while len(stack) > 0:
                node = stack.pop()
                for neigh in adj_list[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    unvisited.remove(neigh)
                    stack.append(neigh)
            
            # Step 2: Run dfs from every node
            max_time = 0
            for visited_node in visited:
                visit_time = {visited_node: 0}
                queue = collections.deque([(0, visited_node)]) # (cur_time, node)
                while len(queue) > 0:
                    cur_time, node = queue.popleft()
                    if max_time < cur_time:
                        max_time = cur_time

                    for neigh in adj_list[node]:
                        if neigh in visit_time:
                            if abs(cur_time + 1 - visit_time[neigh]) % 2 == 1:
                                return -1 # Cannot have odd cycles!
                            continue
                        
                        visit_time[neigh] = cur_time + 1
                        queue.append((cur_time + 1, neigh))
            
            # Max number of groups will be number of nodes in longest path.
            # max_time represents number of EDGES in longest path, hence number
            # of nodes is just max_time + 1
            res += max_time + 1

        return res

# e - a - d - f
#     |       |
#     b - c - g

# a - b

# a - b - c - d - e - ... - z

# G1 G2 G3 G4 G5
# e  a  d  c  g
#       b  f

# A B

# m m'