class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Idea: Topologically sort the elements based on their OUT-degree, not their
        # IN-degree as in the typical topological sort algorithm! Then, we'll start of
        # with our set of nodes with 0 outgoing edges, making them terminal nodes, and
        # "loosening" the constraint for ANY nodes that POINT to 6. Hence, the first step
        # of the algorithm will be to create a hashmap 'd' of nodes to a set/list of nodes 
        # that POINT to them.
        d = defaultdict(set) # node: {node's in-neighbors}, i.e. "reverse" adjacency list
        for node, neighbors in enumerate(graph):
            for neigh in neighbors:
                # node -> neigh, so node is neigh's "in-neighbor"
                d[neigh].add(node)
        
        # print(f"{d=}")
        # return []
        outdegree = [len(neighbors) for neighbors in graph]
        queue = collections.deque(node for node in range(len(graph)) if outdegree[node] == 0)
        topo_order = []
        while len(queue) > 0:
            node = queue.popleft()
            topo_order.append(node)
            for in_neigh in d[node]:
                outdegree[in_neigh] -= 1
                if outdegree[in_neigh] == 0:
                    queue.append(in_neigh)


        topo_order.sort() # The answer should be sorted in ascending order.
        return topo_order
        
        """
        d = {
            6: [] (0),
            5: [] (0),
            4: [5] (1),
            3: [0] (1),
            2: [5] (1),
            1: [2,3] (2),
            0: [1, 2] (2)
        }
        """