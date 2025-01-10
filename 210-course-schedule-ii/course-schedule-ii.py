class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Same thing as Course Schedule I, but this time return the actual topological-sort
        # ordering instead of returning True/False depending on whether the ordering was
        # incomplete or not :p
        adj_list = {course: [] for course in range(numCourses)}
        indegree = {course: 0 for course in range(numCourses)}
        
        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1
        
        topo_order = [course for course in range(numCourses) if indegree[course] == 0]
        queue = collections.deque(topo_order)
        while len(queue) > 0:
            course = queue.popleft()
            for neigh in adj_list[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
                    topo_order.append(neigh)

        # topo_order will be incomplete if there was a cycle in the graph (which
        # is the case if and only if it is impossible to finish all courses, as per
        # the Course Schedule I problem!)
        return topo_order if len(topo_order) == numCourses else []
