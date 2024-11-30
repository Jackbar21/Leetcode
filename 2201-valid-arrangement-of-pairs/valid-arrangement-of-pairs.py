class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Since we're going to use Hierholzer's algorithm (Hint #3), we are gonna apply
        # Hint #2, which I initially thought was clever but unnecessary, since in doing
        # so we represent the pairs via the EDGES and not the NODES of the graph, which
        # is absoluetly perfect for this use case (i.e. with Hierholzer's algorithm) :)
        # As for why Hierholzer's algorithm works, please do not ask me, I have no idea xD

        adj_list = defaultdict(list)
        indegree, outdegree = defaultdict(int), defaultdict(int)
        for start, end in pairs:
            adj_list[start].append(end)
            indegree[end] += 1
            indegree[start] += 0 # to make sure indegree contains every node!
            outdegree[start] += 1
            # outdegree[end] += 0
        
        # For this problem, the node we start with is important... we should feed the
        # one with smallest indegree, then tie break to one with largest outdegree. Additionally,
        # only nodes with EVEN degrees should be considered (degree = indegree + outdegree)!
        start_node = None
        min_value = (True, float("inf"), float("-inf")) # (is-even-degree, indegree, outdegree)
        for node in indegree:
            value = (
                (indegree[node] + outdegree[node]) % 2 == 0, 
                indegree[node], 
                -outdegree[node]
            )
            if value < min_value:
                min_value = value
                start_node = node

        # sorted_arr = sorted(indegree.keys(), key=lambda node: ((indegree[node] + outdegree[node]) % 2 == 0, indegree[node], -outdegree[node]))
        # print(f"{sorted_arr=}")
        # start_node = sorted_arr[0]
        res = self.getCircuit(adj_list, start_node)
        print(f"{res=}")
        print(f"{adj_list=}")
        # return []
        return [
            [res[i - 1], res[i]]
            for i in range(1, len(res))
        ]
        





    #######################################
    ### ONLY GEEKS-FOR-GEEKS CODE BELOW ###
    #######################################

    # Python3 program to print Eulerian circuit in given
    # directed graph using Hierholzer algorithm
    def getCircuit(self, adj, start_node):
        # The GEEKS-FOR-GEEKS algorithm below has been modified as needed for this problem...
    
        # adj represents the adjacency list of
        # the directed graph
        
        if len(adj) == 0:
            return # empty graph
    
        # Maintain a stack to keep vertices
        # We can start from any vertex, here we start with start_node
        curr_path = [start_node]
    
        # list to store final circuit
        circuit = []
    
        while curr_path:
    
            curr_v = curr_path[-1]
            
            # If there's remaining edge in adjacency list  
            # of the current vertex 
            if adj[curr_v]:
    
                # Find and remove the next vertex that is  
                # adjacent to the current vertex
                next_v = adj[curr_v].pop()
    
                # Push the new vertex to the stack
                curr_path.append(next_v)
    
            # back-track to find remaining circuit
            else:
                # Remove the current vertex and 
                # put it in the circuit
                circuit.append(curr_path.pop())
    
        # we've got the circuit, now print it in reverse
        for i in range(len(circuit) - 1, -1, -1):
            print(circuit[i], end = "")
            if i:
                print(" -> ", end = "")
        print()
        return circuit[::-1]