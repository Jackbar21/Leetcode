class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
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
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    stack.append(neigh)
                    d[i].add(neigh)

        return list(v in d[u] for u, v in queries)
