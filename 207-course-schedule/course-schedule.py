class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Idea: Turn the problem into a graph, where for each [a, b] in prerequisites,
        # consider a & b as nodes in the graph, with an edge from b to a representing
        # that one of a's "dependencies" is b (i.e. course b needs to be taken before
        # course a). Then, the answer is true if and only if there are NO cycles in the
        # graph. One such way to discover whether a graph has a cycle or not, which I
        # learned thanks to Neetcode, is to run a topological sort (via indegree method)
        # and check whether one can be created that includes ALL the elements (as otherwise,
        # there must be a cycle!)

        # Step 1: Build an adjacency list of the graph! The keys will be the set of nodes :)
        # Step 2: Get all of the nodes indegrees
        adj_list = {course: [] for course in range(numCourses)}
        indegree = {course: 0 for course in range(numCourses)}
        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1

        # topo_sort = []
        count = 0
        queue = collections.deque([node for node in adj_list if indegree[node] == 0])
        while len(queue) > 0:
            node = queue.popleft()
            # We have popped node from the queue, and hence it is now a course
            # that we have "taken". Hence, ANY other course that has this course
            # as a dependency, can now have that extra constraint relaxed :)
            # In other words, relax this constraint for all of this node's NEIGHBORS.
            # topo_sort.append(node)
            count += 1

            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # return len(topo_sort) == len(adj_list)
        return count == numCourses

"""    
CSCB36 <-- CSCA67, CSCA48
CSCA48 <-- CSCA08

adj_list = {
    "CSCA67": ["CSCB36"],
    "CSCA48": ["CSCB36"],
    "CSCA08": ["CSCA48"],
    "CSCB36": []
}

indegrees = {
    "CSCB36": 0,
    "CSCA48": 0,
    "CSCA67": 0,
    "CSCA08": 0
}

count = 4

queue = []
"""