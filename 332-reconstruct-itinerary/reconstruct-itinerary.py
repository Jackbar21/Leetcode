class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(lambda: defaultdict(int))
        for u, v in tickets:
            adj_list[u][v] += 1
        
        itinerary = ["JFK"]
        def backtrack():
            if len(itinerary) == len(tickets) + 1:
                return True # To end all backtrack calls!

            node = itinerary[-1]
            neighbor_dict = {neigh: freq for neigh, freq in adj_list[node].items() if freq > 0}
            sorted_neighbors = sorted(neighbor_dict)

            for neigh in sorted_neighbors:
                # if neighbor_dict[neigh] == 0:
                #     continue

                adj_list[node][neigh] -= 1
                itinerary.append(neigh)
                if backtrack():
                    return True
                itinerary.pop()
                adj_list[node][neigh] += 1
            
            return False
        
        backtrack()
        return itinerary
