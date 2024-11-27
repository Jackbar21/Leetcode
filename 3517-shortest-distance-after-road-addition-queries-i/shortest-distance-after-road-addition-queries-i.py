class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Idea: since all edges have same weight, Dijkstra's is overkill and we can simply
        # use BFS. Initialize an adjacency list as per problem description, then after each
        # query add a new edge into adjacency list, and call BFS from 0 to n - 1 every single
        # time to get the new shortest path. It's pretty brute force, but it works just fine :)
        SOURCE, DEST = 0, n - 1
        adj_list = {i: set() for i in range(n)}
        for i in range(n - 1):
            u, v = i, i + 1
            adj_list[u].add(v)

        answer = []
        for (u, v) in queries:
            adj_list[u].add(v)
            
            # BFS
            queue = collections.deque([(SOURCE, 0)]) # (node, cost)
            visited = set([SOURCE])
            while len(queue) > 0:
                node, cost = queue.popleft()
                if node == DEST:
                    answer.append(cost)
                    break

                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, cost + 1))
            
            # 1 is shortest possible path, so all remaining paths will
            # have same best-possible-cost of 1 :)
            if answer[-1] == 1:
                return answer + [1] * (len(queries) - len(answer))
        
        return answer
