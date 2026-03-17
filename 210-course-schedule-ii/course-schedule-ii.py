class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {node: set() for node in range(numCourses)}
        indegree = {node: 0 for node in range(numCourses)}

        for a, b in prerequisites:
            adj_list[b].add(a)
            indegree[a] += 1

        topo_sort = []
        queue = collections.deque([node for node in range(numCourses) if indegree[node] == 0])
        while queue:
            node = queue.popleft()
            topo_sort.append(node)

            # Now, node is no longer a prerequisite for any other course. 
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        if len(topo_sort) < numCourses:
            # There was a cycle in the graph, no solution
            return []
        
        return topo_sort
