class Solution:
    def checkIfPrerequisiteNaive(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build an adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)

        # Step 2: For each node, run a DFS from that node to find all the courses it is a prerequisite of
        d = [set() for _ in range(numCourses)] # node is a prerequisite of every course in d[node]
        for i in range(numCourses):
            stack = [i]
            visited = set([i])
            while len(stack) > 0:
                node = stack.pop()

                for neigh in adj_list[node]:
                    if neigh not in visited:
                        continue
                    visited.add(neigh)
                    stack.append(neigh)
                    d[i].add(neigh)

        return [v in d[u] for u, v in queries]

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build an adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)

        # We know from constraints that prerequisites graph has NO cycles!!!
        # This means we have a DAG, which is perfect for something like DP!
        @cache
        def dp(node):
            # Can add node as its own child, since constraints 
            # guarantee that u != v for any (u,v) in queries!
            children = set([node])
            for neigh in adj_list[node]:
                children.update(dp(neigh))
            return children

        return [v in dp(u) for u, v in queries]
