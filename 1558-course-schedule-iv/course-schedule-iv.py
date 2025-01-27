class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build an adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)

        # Step 2: For each node, run a DFS from that node to find all the courses it is a prerequisite of
        d = [set() for _ in range(numCourses)] # node is a prerequisite of every course in d[node]
        for i in range(numCourses):
            queue = collections.deque([i])
            visited = set([i])
            while len(queue) > 0:
                node = queue.popleft()

                for neigh in adj_list[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    queue.append(neigh)
                    d[i].add(neigh)
        
        # res = []
        # for u, v in queries:
        #     res.append(v in d[u])
        # return res
        return list(map(lambda query: (query[1] in d[query[0]]), queries))
