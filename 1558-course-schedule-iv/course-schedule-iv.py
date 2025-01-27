class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build an adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)

        # We know from constraints that prerequisites graph has NO cycles!!!
        # This means we have a DAG, which is perfect for something like DP!
        @cache
        def getChildren(node):
            # Can add node as its own child, since constraints 
            # guarantee that u != v for any (u,v) in queries!
            children = set(adj_list[node])
            for neigh in adj_list[node]:
                children.update(getChildren(neigh))
            return children

        return [v in getChildren(u) for u, v in queries]
