class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source, dest, price in flights:
            adj_list[source].append((dest, price)) # (neigh, price)

        @cache
        def dp(node, edges_left):
            if node == dst:
                return 0

            if edges_left == 0:
                return float("inf")
            
            return min(
                (price + dp(neigh, edges_left - 1) for neigh, price in adj_list[node]), 
                default = float("inf")
            )

        res = dp(src, k + 1)
        return res if res != float("inf") else -1
