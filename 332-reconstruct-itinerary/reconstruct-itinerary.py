class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # assert len(tickets) == len(set(tuple(ticket) for ticket in tickets))

        adj_list = defaultdict(lambda: defaultdict(int))
        indegree = defaultdict(int)
        for u, v in tickets:
            adj_list[u][v] += 1
            indegree[v] += 1
        
        #print(f"{indegree=}")
        
        itinerary = ["JFK"]
        self.res = None
        def backtrack():
            #print(f"{itinerary=}")
            #print(f"{adj_list=}")
            if len(itinerary) == len(tickets) + 1:
                self.res = [airport for airport in itinerary]
                return True # To end all backtrack calls!

            node = itinerary[-1]
            neighbor_dict = adj_list[node]
            sorted_neighbors = sorted(neighbor_dict)
            # if len(sorted_neighbors) == 0:
            #     # itinerary.pop()
            #     return

            for neigh in sorted_neighbors:
                assert neighbor_dict[neigh] >= 0
                if neighbor_dict[neigh] == 0:
                    continue
                # adj_list[node].remove(neigh)
                neighbor_dict[neigh] -= 1
                itinerary.append(neigh)
                if backtrack():
                    return True
                # assert itinerary.pop() == neigh
                itinerary.pop()
                # adj_list[node].add(neigh)
                neighbor_dict[neigh] += 1
            
            return False
        
        # #print(f"{list(backtrack())=}")
        # for res in backtrack():
        #     return res # Return the first!
        # return None
        backtrack()
        return self.res
            
        
        # for node in adj_list:
        #     neighbors = adj_list[node]
        #     for i in range(len(neighbors)):
        #         node = neighbors[i]
        #         neighbors[i] = (indegree[node], node)
        
        # #print(f"{adj_list=}")

        # queue = collections.deque()

        # node = "JFK"
        # res = []
        # while True:
        #     res.append(node)
        #     neighbors = adj_list[node]
        #     if len(neighbors) == 0:
        #         #print(f"{res=}")
        #         # assert len(res) == len(tickets) + 1
        #         return res
        #         # break

        #     best_neigh, max_degree = None, float("-inf")
        #     for neigh in sorted(neighbors):
        #         if max_degree < (degree := indegree[neigh]):
        #             best_neigh = neigh
        #             max_degree = degree
            
        #     # Loop Invariant
        #     adj_list[node].remove(best_neigh)
        #     indegree[best_neigh] -= 1
        #     node = best_neigh
        
        
        # # Heapify adj_list
        # # for node in adj_list:
        # #     heapq.heapify(adj_list[node])
        
        
        # itinerary = []
        # airport = "JFK"
        # while True:
        #     itinerary.append(airport)

        #     if len(adj_list[airport]) == 0:
        #         break
            
        #     # Loop Invariant
        #     airport = heapq.heappop(adj_list[airport])
        
        # return itinerary
            