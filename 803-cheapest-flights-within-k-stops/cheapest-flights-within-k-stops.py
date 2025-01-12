class Solution:
    def dp(self, node, edges_left):
        if (node, edges_left) in self.memo:
            return self.memo[(node, edges_left)]

        if node == self.dst:
            return 0

        if edges_left == 0:
            return float("inf")
        
        res = float("inf")
        for neigh, price in self.adj_list[node]:
            path_cost = price + self.dp(neigh, edges_left - 1)
            if path_cost < res:
                res = path_cost
        
        self.memo[(node, edges_left)] = res
        return res


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, dest, price in flights:
            adj_list[source].append((dest, price)) # (neigh, price)
        self.dst, self.adj_list, self.memo = dst, adj_list, {}

        res = self.dp(src, k + 1)
        return res if res != float("inf") else -1
