class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1
        
        queue = deque([node for node in range(numCourses) if indegree[node] == 0])
        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return topo if len(topo) == numCourses else []
