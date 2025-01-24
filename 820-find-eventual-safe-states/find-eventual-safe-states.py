class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Idea: Topologically sort the elements based on their OUT-degree, not their
        # IN-degree as in the typical topological sort algorithm! Then, we'll start of
        # with our set of nodes with 0 outgoing edges, making them terminal nodes, and
        # "loosening" the constraint for ANY nodes that POINT to 6. Hence, the first step
        # of the algorithm will be to create a hashmap 'd' of nodes to a set/list of nodes 
        # that POINT to them.
        N = len(graph)
        d = [[] for _ in range(N)] # node: {node's in-neighbors}, i.e. "reverse" adjacency list
        outdegree = []
        good_nodes = [] # A node is "good" if it is terminal OR safe!
        for node, neighbors in enumerate(graph):
            for neigh in neighbors:
                d[neigh].append(node)
            
            degree = len(neighbors)
            outdegree.append(degree)
            if degree == 0:
                good_nodes.append(node) # Terminal node, hence "good"
        
        topo_order = []
        while good_nodes:
            node = good_nodes.pop()
            topo_order.append(node)
            for in_neigh in d[node]:
                outdegree[in_neigh] -= 1
                if outdegree[in_neigh] == 0:
                    # Node is safe, hence "good"
                    good_nodes.append(in_neigh)

        topo_order.sort() # The answer should be sorted in ascending order.
        return topo_order
