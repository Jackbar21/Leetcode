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
        def backtrack():
            #print(f"{itinerary=}")
            #print(f"{adj_list=}")
            if len(itinerary) == len(tickets) + 1:
                yield [airport for airport in itinerary]
                return

            node = itinerary[-1]
            sorted_neighbors = sorted(adj_list[node])
            # if len(sorted_neighbors) == 0:
            #     # itinerary.pop()
            #     return

            for neigh in sorted_neighbors:
                assert adj_list[node][neigh] >= 0
                if adj_list[node][neigh] == 0:
                    continue
                # adj_list[node].remove(neigh)
                adj_list[node][neigh] -= 1
                itinerary.append(neigh)
                yield from backtrack()
                assert itinerary.pop() == neigh
                # adj_list[node].add(neigh)
                adj_list[node][neigh] += 1
        
        # #print(f"{list(backtrack())=}")
        for res in backtrack():
            return res # Return the first!
        return None
            
        
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
            