class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        adj_list = [set() for i in range(N)]
        indegree = [0] * N
        for i in range(len(ratings)):
            prev = ratings[i - 1] if i > 0 else float("inf")
            cur = ratings[i]
            nxt = ratings[i + 1] if i + 1 < N else float("inf")

            if cur > prev:
                # cur (index i) needs MORE candy than prev (index i - 1)
                # adj_list[i - 1].add(i)
                # indegree[i] += 1
                adj_list[i].add(i - 1)
                indegree[i - 1] += 1
            
            if cur > nxt:
                # cur (index i) needs MORE candy than prev (index i - 1)
                # adj_list[i + 1].add(i)
                # indegree[i] += 1
                adj_list[i].add(i + 1)
                indegree[i + 1] += 1
        
        # Run a topo sort, but get the depth of each node
        # queue = collections.deque()
        # print(f"{adj_list}")
        for i in range(N):
            print(f"{i}: {adj_list[i]=}")
        print()
        for i in range(N):
            print(f"{i}: {indegree[i]=}")
        
        @cache
        def dp(node):
            if len(adj_list[node]) == 0:
                return 1 # Doesn't need more candy than anybody else, so just 1 candy!
            
            return 1 + max(dp(neigh) for neigh in adj_list[node])
        
        return sum(dp(i) for i in range(N))

        
        # return N + sum(indegree[node] > 0 for node in range(N))

        # # return N + sum(indegree)
        depths = [0] * N

        queue = collections.deque((0, node) for node in range(N) if indegree[node] == 0)
        visited = set(queue)
        while queue:
            depth, node = queue.popleft()
            # assert depths[node] == -1
            # depths[node] = depth
            # print(f"{node=}, {depth=}")
            depths[node] = max(depth, depths[node])

            for neigh in adj_list[node]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                queue.append((depth + 1, node))
        
        print(f"{depths=}")
        return N + sum(depths)
