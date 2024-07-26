class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # E = edges
        # V = {0,1,2,...,n} = {i : 0 <= i < n}
        # L(u,v,k) = min. weight of u->v k path
        # L(u,v,k) = min ({L(u,v,k-1)} U {L(u,w,k-1) + wt(w,v) : (w,v) \in E})
        # u->v k-1, (w,v)

        #           <= k-1          <= k-1
        # p = i -------------k-------------------> j , k

        # C(i,j,k) = min weight of an i->j k path (inf. if no such path)
        #             forall i,j in V (where V = {0,1,...,n-1}), 
        #             forall 0 <= k < n

        # Case 1: k is *not* an intermediate node on p
        #         C(i,j,k) = C(i,j,k-1)

        # Case 2: k is intermediate node on p
        #         C(i,j,k) = C(i,k,k-1) + C(k,j,k-1)

        # (+) 
        # C(i,j,k) = {
        #    0,         if i==j and k = -1
        #    wt(i,j),   if (i,j)\in edges and k = -1
        #    INF,       if (i,j)\not\in edges and k = -1
        #    min{ C(i,j,k-1), C(i,k,k-1) + C(k,j,k-1) }
        # }

        # FW(G,wt):
        # initialize C(i,j,0) forall i,j\in V as in (+)
        # for k := 1 to n do
        #   for i := 1 to n do
        #     for j := 1 to n do
        #       C(i,j,k) := min(C(i,j,k-1), C(i,k,k-1) + C(k,j,k-1))
        # return C(-,-,n)

        # Running Time: O(n^3)
        # Space Complexity: O(n^3) naively
        #                   O(n^2) suffices (only store least two 3D "cds")

        edge_dict = {}
        for edge in edges:
            u,v,cost = edge
            edge_dict[(u,v)] = cost

        # k == -1 setup
        dp = [[float("inf")]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = 0
                elif (i,j) in edge_dict or (j,i) in edge_dict:
                    dp[i][j] = edge_dict[(i,j)] if (i,j) in edge_dict else edge_dict[(j,i)]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    case1 = dp[i][j]
                    case2 = dp[i][k] + dp[k][j]
                    dp[i][j] = min(case1, case2)
        
        cities_dict = {i: set() for i in range(n)}
        for i in range(n):
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    cities_dict[i].add(j)
                    cities_dict[j].add(i)
        
        shortest_len = float("inf")
        city = -1
        for i in range(n):
            if len(cities_dict[i]) <= shortest_len:
                shortest_len = len(cities_dict[i])
                city = i
        
        return city        